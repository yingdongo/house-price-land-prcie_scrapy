# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class LandItem(scrapy.Item):
    title = scrapy.Field()
    district_id = scrapy.Field()
    land_id = scrapy.Field()
    total_land_area = scrapy.Field()
    construction_land_area = scrapy.Field()
    floor_area = scrapy.Field()
    plot_ratio = scrapy.Field()
    commercial_ratio = scrapy.Field()
    land_usage = scrapy.Field()
    location = scrapy.Field()
    trade_result = scrapy.Field()
    trade_time = scrapy.Field()
    trade_form = scrapy.Field()
    buyer = scrapy.Field()
    starting_price = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    writeTime = scrapy.Field()



class CommunityItem(scrapy.Item):
    community_id = scrapy.Field()
    community_name = scrapy.Field()
    community_average_price = scrapy.Field()
    building_age = scrapy.Field()
    district = scrapy.Field()
    district_id = scrapy.Field()
    level = scrapy.Field()
    year = scrapy.Field()
    month = scrapy.Field()
    writeTime = scrapy.Field()

