# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy_redis.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from bs4 import BeautifulSoup
from zhihu.items import ZhihuItem
from scrapy.dupefilters import RFPDupeFilter

class ZhiHu(CrawlSpider):
    '''
    spider that reads urls from start_urls
    '''

    name = "zhihu"
    allowed_domains = ['www.zhihu.com']
    start_urls = [
        "https://www.zhihu.com/question/51453506"
    ]

    # 定义next规则
    rules = [
        # 提取问题详情链接并处理
        Rule(SgmlLinkExtractor(allow = [r'/question/\d{8}$',r'https://www.zhihu.com/question/\d{8}$' ]),callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        item = ZhihuItem()
        soup = BeautifulSoup(response.body, "lxml")

        # 问题url
        item["question_url"] = response.url
        # 提问问题的人
        item["question_author"] = "未知"

        # 问题标题
        title_list = soup.find(attrs={"class":"zm-item-title"})
        title = title_list.find(attrs={"class":"zm-editable-content"}).string
        item["question_title"] = title

        # 回答者和回答的内容
        answer_author_content = []
        # 回答者
        content_author = soup.findAll(attrs={"class":"zm-item-answer  zm-item-expanded"})
        for tag in content_author:
            if tag.find(attrs={"class":"author-link"}) is None:
                answer_author = tag.find(attrs={"class":"name"}).string
            else:
                answer_author = tag.find(attrs={"class":"author-link"}).string

            # 回答的内容
            answer_contents = tag.findAll(attrs={"class":"zm-editable-content clearfix"})

            contents = []
            for answer in answer_contents:
                for i in answer.stripped_strings:
                    content = str(i).replace("<p>","").replace("</p>","").replace("<br>","").replace("<br/>","").replace("<b>","").replace("</b>","").replace("b/","").replace(" ", "")
                    contents.append(str(content))

            # 组合name and content
            if (answer_author != None) and (contents != None):
                ans_author = {}
                ans_author["author"] = answer_author
                ans_author["content"] = contents
                answer_author_content.append(ans_author)
        item["author_content"] = answer_author_content

        # 问题类型
        type_list = soup.findAll(attrs={"class":"zm-tag-editor-labels zg-clear"})
        if len(type_list):
            types = []
            for type in type_list[0].findAll('a'):
                if (type != None):
                    # print "类型++++++++++++++++++++++++++++++++++++++++++++++++++++：", type.string.replace("\n", "")
                    types.append(type.string.strip())

            item["question_type"] = types
        yield item
