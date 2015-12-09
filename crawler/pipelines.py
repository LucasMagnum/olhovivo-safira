# coding: utf-8

from collections import defaultdict


class GroupResourcesByMonth(object):
    def process_item(self, item, spider):
        resources_by_month = item.get('resources_by_month', [])

        grouped_resources = defaultdict(float)

        for resource in resources_by_month:
            grouped_resources[resource['month']] += self.clean_value(resource['value'])

        item['resources_by_month'] = grouped_resources
        return item

    def clean_value(self, value):
        """ Generally value is in format X.XXX,XX """
        return float(value.replace('.', '').replace(',', '.'))
