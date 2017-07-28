# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy.item import Item, Field
#from scrapy.contrib.loader import XPathItemLoader
#from scrapy.contrib.loader.processor import TakeFirst

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
#class WebsiteLoader(XPathItemLoader):
#	default_item_class = SoftmoniItem
#	default_output_processor = TakeFirst()
