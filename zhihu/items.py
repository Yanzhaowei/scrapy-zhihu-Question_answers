# -*- coding: utf-8 -*-

from scrapy.item import Item, Field
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import MapCompose, TakeFirst, Join

class ZhihuItem(Item):
    question_author = Field()      # 提问者的姓名
    question_title = Field()       # 问题的标题
    author_content = Field()       # 回答者和回答的内容
    question_type = Field()        # 问题所属类别
    question_url = Field()         # 问题的URL

    crawled = Field()
    spider = Field()


class ZhihuLoader(ItemLoader):
    default_item_class = ZhihuItem
    default_input_processor = MapCompose(lambda  s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()
