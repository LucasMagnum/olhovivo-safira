# coding: utf-8

import scrapy

from scrapy.selector import Selector

from crawler.items import ResourceItem, DepartmentItem


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
            item['action'] = self.extract(columns[1], 'a/text()')
            item['action_link'] = self.extract(columns[1], 'a/@href')
            item['language_person'] = self.extract(columns[2], 'text()')
            item['total_year'] = self.extract(columns[3], 'text()')

            yield item
            yield scrapy.Request(response.urljoin(item['action_link']),
                                 callback=self.parse_department)

    def parse_department(self, response):
        selector = Selector(response)

        for row in selector.xpath(PageConfig.table_rows)[1:]:
            columns = row.xpath('td')

            item = DepartmentItem()
            item['cnpj'] = self.extract(columns[0], 'a/text()')
            item['name'] = self.extract(columns[1], 'text()')

            yield item

    def extract(self, item, xpath):
        return item.xpath('normalize-space({})'.format(xpath)).extract()[0]
