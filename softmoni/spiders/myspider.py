# -*- coding: utf-8 -*-

import scrapy
from softmoni.items import ImagedownloadItem

class SoftmoniSpider(scrapy.Spider):
	name = 'softmonispider'
	start_urls = ['https://en.softonic.com/windows/best-software']

	def parse(self, response): 
		for item in response.css('li.list-program-item'): 
			path = item.css('a ::attr(href)').extract_first()
			yield scrapy.Request(path, callback = self.parseDetails)
    		#yield scrapy.Request(path + '/download', callback = self.download)

        #next_page = response.css('a.pagination-next ::attr(href)').extract_first()
        #if next_page:
        #    yield scrapy.Request(response.urljoin(next_page), callback=self.parse)


	def parseDetails(self, response): 
		title = repr(response.css('h1.media-app__title ::text').extract_first()) 
		description = repr(response.css('article.app-softonic-review__content').extract_first()) 
		screenshots = repr(response.css('a.gallery__media-links ::attr(href)').extract()) 
		os = repr(response.css('p.app-specs__value[itemprop=operatingSystem] ::text').extract_first()) 
		dl = repr(response.css('div.app-specs li:nth-child(3) p ::text').extract_first()) 
		#yield ImagedownloadItem( 
			#	image_urls = screenshots 
			#) 
		yield { 
			'title': title, 
			'description': description, 
			'os': os, 
			} 


	def download(self, response): 
		file = response.css('input#url_download_free ::attr(value)').extract() 
		if file: 
			yield FiledownloadItem( 
				file_urls = file 
				) 
		else: 
			file = response.css('#box-download a ::attr(href)').extract()

