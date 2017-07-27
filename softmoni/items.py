# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SoftmoniItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    os = scrapy.Field()

class ImagedownloadItem(scrapy.Item):
    image_urls = scrapy.Field()
    files = scrapy.Field()
class FiledownloadItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
pass
