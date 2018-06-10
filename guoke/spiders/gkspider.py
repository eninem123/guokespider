# -*- coding: utf-8 -*-
import scrapy,re

from guoke.items import GuokeItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule

from guoke.items import GuokeItem,GuokeItem2

class GkspiderSpider(CrawlSpider):
    name = 'gkspider'
    allowed_domains = ['www.guokr.com']
    base_url = 'https://www.guokr.com/'
    start_urls = ['https://www.guokr.com/ask/highlight/?page=1']
    rules = [
        Rule(LinkExtractor(allow=r"ask/highlight/\?page=\d+"), callback="parse_page", follow=True),
        Rule(LinkExtractor(allow=r"question/\d+"), callback="parse_position", follow=False)
    ]
    def parse(self, response):
        data_list = response.xpath("//div[@class='ask-list-detials']")
        for data in data_list:
            item = GuokeItem()
            item['title']=data.xpath("./h2/a/text()").extract_first()
            item['info']=data.xpath("./p/text()").extract_first()

            yield item

        # if '下一页' in response.xpath("//ul[@class='gpages']/li/a/text()").extract():
        #     next_url = self.base_url + response.xpath("//ul[@class='gpages']/li[last()-1]/a/@href").extract_first()
        #     yield scrapy.Request(next_url, callback=self.parse)


    def parse_position(self, response):
        item = GuokeItem2()
        data_list = response.xpath("//p[@class='answer-usr']")
        for data in data_list:
            item['name'] =data.xpath('./a/text()').extract_first()

            yield item