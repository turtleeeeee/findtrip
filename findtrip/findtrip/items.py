# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FindtripItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    site = scrapy.Field()
    airports = scrapy.Field()
    price = scrapy.Field()
    plane_info = scrapy.Field()
    departure_time = scrapy.Field()
    departure_airport = scrapy.Field()
    arrive_time = scrapy.Field()
    arrive_airport = scrapy.Field()
    cabin_class = scrapy.Field()
    transfer_duration = scrapy.Field()
