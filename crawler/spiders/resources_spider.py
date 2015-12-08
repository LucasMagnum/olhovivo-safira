# coding: utf-8

import scrapy

from scrapy.selector import Selector

from crawler.items import ResourceItem


class PageConfig(object):
    host = 'http://www.portaltransparencia.gov.br'
    resources_url = '/PortalTransparenciaListaAcoes.asp?Exercicio=2015&SelecaoUF=1&SiglaUF=MG&CodMun=5259'

    table_rows = '//*[@id="listagem"]/table/tr'


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

            request = scrapy.Request(response.urljoin(resource_link),
                                     callback=self.parse_department)
            request.meta['resource_item'] = item
            yield request

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
        resource_item = response.meta['resource_item']
        selector = Selector(response)

        resources_by_month = []

        for row in selector.xpath(PageConfig.table_rows)[1:]:
            columns = row.xpath('td')
            resource = {
                'month': self.extract(columns[0], 'text()'),
                'value': self.extract(columns[5], 'text()'),
            }
            resources_by_month.append(resource)

        resource_item['resources_by_month'] = resources_by_month
        yield resource_item

    def extract(self, item, xpath):
        return item.xpath('normalize-space({})'.format(xpath)).extract()[0]
