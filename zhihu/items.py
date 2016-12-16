# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class ZhihuItem(Item):
    question_author = Field()      # 提问者的姓名
    question_title = Field()       # 问题的标题
    author_content = Field()       # 回答者和回答的内容
    question_type = Field()        # 问题所属类别
    question_url = Field()         # 问题的URL
