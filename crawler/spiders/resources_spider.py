# coding: utf-8

from urllib import urlencode
from urllib2 import urlparse

import scrapy

from scrapy.selector import Selector

from crawler.items import ResourceItem


class PageConfig(object):
    host = 'http://www.portaltransparencia.gov.br'
    resources_url = '/PortalTransparenciaListaAcoes.asp?Exercicio=2015&SelecaoUF=1&SiglaUF=MG&CodMun=5259'

    table_rows = '//*[@id="listagem"]/table/tr'
    paginate_info = '//*[@id="paginacao"]/p[1]/text()'

    ignored_details = [
        u'8442 - Transfer\xeancia de Renda Diretamente \xe0s Fam\xedlias em Condi\xe7\xe3o de Pobreza e Extrema Pobreza (Lei n\xba 10.836, de 2004)'
    ]


class ResourceSpider(scrapy.Spider):
    name = 'resources'
    allowed_domains = ['portaltransparencia.gov.br']
    start_urls = [
        '{}{}'.format(PageConfig.host, PageConfig.resources_url)
    ]

    def parse(self, response):
        selector = Selector(response)

        for row in selector.xpath(PageConfig.table_rows)[1:]:
            columns = row.xpath('td')

            item = ResourceItem()
            item['category'] = self.extract(columns[0], 'text()')
            item['description'] = self.extract(columns[1], 'a/text()')
            item['total_year'] = self.extract(columns[3], 'text()')

            resource_link = self.extract(columns[1], 'a/@href')

            # For while ignore "Bolsa Familia"
            if item['description'] in PageConfig.ignored_details:
                yield item
            else:
                request = scrapy.Request(response.urljoin(resource_link),
                                         callback=self.parse_department)
                request.meta['resource_item'] = item
                yield request

        next_page_link = self.get_next_page_link(response)
        if next_page_link:
            yield scrapy.Request(response.urljoin(next_page_link), callback=self.parse)

    def parse_department(self, response):
        resource_item = response.meta['resource_item']
        selector = Selector(response)

        for row in selector.xpath(PageConfig.table_rows)[1:]:
            columns = row.xpath('td')

            resource_item['department_cnpj'] = self.extract(columns[0], 'a/text()')
            resource_item['department_name'] = self.extract(columns[1], 'text()')

            link_details = self.extract(columns[0], 'a/@href')

            request = scrapy.Request(response.urljoin(link_details),
                                     callback=self.parse_resources_by_month)
            request.meta['resource_item'] = resource_item
            yield request

    def parse_resources_by_month(self, response):
        item = response.meta['resource_item']
        selector = Selector(response)

        resources_by_month = []

        for row in selector.xpath(PageConfig.table_rows)[1:]:
            columns = row.xpath('td')
            resource = {
                'month': self.extract(columns[0], 'text()'),
                'value': self.extract(columns[5], 'text()'),
            }
            resources_by_month.append(resource)

        item['resources_by_month'] = item.get('resources_by_month', []) + resources_by_month

        next_page_link = self.get_next_page_link(response)
        if next_page_link:
            request = scrapy.Request(response.urljoin(next_page_link),
                                     callback=self.parse_resources_by_month)
            request.meta['resource_item'] = item
            yield request
        else:
            yield item

    def get_next_page_link(self, response):
        """
            >> page_info = u"Página 1/2"
            >> paginate_index = "1/1"
            >> all_pages_visited = paginate_index == paginate_index[::-1]

            # change querystring to include +1 in `Pagina`
            >> query_params['Pagina'] = int(query_params.get('Pagina', 1))
        """
        page_info = self.extract(response, PageConfig.paginate_info)
        page_index = page_info.split()[1]

        all_pages_visited = page_index == page_index[::-1]

        if not all_pages_visited:
            scheme, netloc, path, query_string, fragment = urlparse.urlsplit(response.url)
            query_params = dict(urlparse.parse_qsl(query_string))

            # Update page number
            query_params['Pagina'] = int(query_params.get('Pagina', 1)) + 1
            new_querystring = urlencode(query_params, doseq=True)

            return urlparse.urlunsplit((scheme, netloc, path, new_querystring, fragment))

    def extract(self, item, xpath):
        return item.xpath('normalize-space({})'.format(xpath)).extract()[0]
