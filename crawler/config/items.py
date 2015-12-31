# coding: utf-8

import scrapy


class ResourceItem(scrapy.Item):
    category = scrapy.Field()
    description = scrapy.Field()

    total_year = scrapy.Field()

    department_cnpj = scrapy.Field()
    department_name = scrapy.Field()

    resources_by_month = scrapy.Field()
    grouped_resources_by_month = scrapy.Field()


class PersonItem(scrapy.Item):
    name = scrapy.Field()
    total_year = scrapy.Field()
