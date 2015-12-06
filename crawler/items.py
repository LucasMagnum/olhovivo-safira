# coding: utf-8

import scrapy


class ResourceItem(scrapy.Item):
    category = scrapy.Field()
    action = scrapy.Field()
    action_link = scrapy.Field()
    language_person = scrapy.Field()
    total_year = scrapy.Field()


class DepartmentItem(scrapy.Item):
    cnpj = scrapy.Field()
    name = scrapy.Field()


class PersonItem(scrapy.Item):
    name = scrapy.Field()
    total_year = scrapy.Field()
