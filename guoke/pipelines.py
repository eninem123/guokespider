# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from guoke.items import GuokeItem,GuokeItem2
import json,re
class GuokePipeline(object):


    def open_spider(self, spider):
        self.f = open("gbk1.txt", "w")

    # 必须实现的，用来处理每一个item数据
    def process_item(self, item, spider):
        if isinstance(item, GuokeItem):
            item['title'] = item['title'].strip()
            item['info'] = item['info'].strip()
            content = json.dumps(dict(item), ensure_ascii=False)

            self.f.write(content)

            self.f.write('\n')

        return item

    # 爬虫关闭时执行一次
    def close_spider(self, spider):
        self.f.close()


class PositionJsonPipeline(object):

    # 爬虫启动时执行一次
    def open_spider(self, spider):
        self.f = open("position1.txt", "w")

    # 必须实现的，用来处理每一个item数据
    def process_item(self, item, spider):
        if isinstance(item, GuokeItem2):
            content = json.dumps(dict(item)) + ",\n"
            self.f.write(content)
        return item

    # 爬虫关闭时执行一次
    def close_spider(self, spider):
        self.f.close()