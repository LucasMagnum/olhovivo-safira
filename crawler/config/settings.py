# -*- coding: utf-8 -*-

BOT_NAME = 'crawler'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

ITEM_PIPELINES = {
    'config.pipelines.GroupResourcesByMonth': 0,
}

RESOURCES_CONFIGS = {
    'ano': 2015,
    'uf': 1,
    'uf_sigla': 'MG',
    'municipio': 5259
}
