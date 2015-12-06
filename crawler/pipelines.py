# coding: utf-8

from scrapy.exceptions import DropItem

from crawler.items import DepartmentItem


class DuplicatesDepartments(object):

    def __init__(self):
        self.cnpjs = set()

    def process_item(self, item, spider):
        if isinstance(item, DepartmentItem):
            if item['cnpj'] in self.cnpjs:
                raise DropItem("Duplicate item found: %s" % item)
            self.cnpjs.add(item['cnpj'])
        return item
