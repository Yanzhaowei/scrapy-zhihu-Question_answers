# -*- coding:utf-8-*-
from scrapy_redis.spiders import RedisCrawlSpider

class MySpider(RedisCrawlSpider):
    """spider that redis urls from redis queue"""
    name = "mySpider_redis"
    redis_key = "mySpider: start_urls"

    def __Init__(self, *args, **kwargs):
        domain = kwargs.pop("domain", '')
        self.allowed_mains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        return {
            "question_author": response.url,
        }