# -*- coding: utf-8 -*-
from fake_useragent import UserAgent
ua = UserAgent()

SPIDER_MODULES = ['lianjia_scrapy.spiders']
NEWSPIDER_MODULE = 'lianjia_scrapy.spiders'
# DEFAULT_ITEM_CLASS = 'lianjia_scrapy.items.LandItem'


DEFAULT_ITEM_CLASS = 'lianjia_scrapy.items.CommunityItem'



ITEM_PIPELINES = {'lianjia_scrapy.pipelines.FilterWordsPipeline': 1}



ITEM_PIPELINES = {
   'lianjia_scrapy.pipelines.MySQLCommunityPipeline': 401,
}

# ITEM_PIPELINES = {
#    'lianjia_scrapy.pipelines.MySQLLandPipeline': 402,
# }



BOT_NAME = 'lianjia_scrapy'

DOWNLOAD_DELAY = .3
ROBOTSTXT_OBEY = False
USER_AGENT = ua.random