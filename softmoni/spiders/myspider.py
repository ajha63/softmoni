# -*- coding: utf-8 -*-

import scrapy
from softmoni.items import ImagedownloadItem

class SoftmoniSpider(scrapy.Spider):
	name = 'softmonispider'
	start_urls = ['https://en.softonic.com/windows/best-software']

	def parse(self, response): 
		IND = 1
		for item in response.xpath('//li[@class=$val]', val='list-program-item js-listed-program'):
			strpath = '//*[@id="program_list"]/li[{:d}]/a/@href'.format(IND)
			path = item.xpath(strpath).extract_first()
			yield scrapy.Request(path, callback = self.parseDetails)
			IND += 1 
			#yield scrapy.Request(path + '/download', callback = self.download) 

		next_page = response.css('a.pagination-next ::attr(href)').extract_first() 
		if next_page: 
			yield scrapy.Request(response.urljoin(next_page), callback=self.parse)


	def parseDetails(self, response): 
		name = response.xpath('//h1[@class=$val]/text()', val='media-app__title').extract_first()
		vers = response.xpath('//h1[@class=$val]/span/text()', val='media-app__title').extract_first()
		try: 
			title = '{:s} {:s}'.format(name, vers)
		except:
			title = '{:s}'.format(name)
		description = response.xpath('normalize-space(.//*[@id="app-softonic-review"]/article)').extract_first()
		os = response.xpath('normalize-space(.//p[@itemprop=$val]/text())', val='operatingSystem').extract_first()
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

