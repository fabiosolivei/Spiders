# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstspyderItem(scrapy.Item):
    # define the fields for your item here like:
    price = scrapy.Field()
    trip = scrapy.Field()
    test = scrapy.Field()
    pass
