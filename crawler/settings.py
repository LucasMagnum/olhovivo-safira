# -*- coding: utf-8 -*-

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

ITEM_PIPELINES = {
    'crawler.pipelines.GroupResourcesByMonth': 0,
}

RESOURCES_CONFIGS = {
    'ano': 2015,
    'uf': 1,
    'uf_sigla': 'MG',
    'municipio': 5259
}
