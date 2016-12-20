# coding=utf-8
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class MyCrawler(RedisCrawlSpider):
    """spider that redis urls from redis queue"""
    name = "myCrawler_redis"
    redis_key = "myCrawler: start_urls"

    rules = (
        Rule(LinkExtractor(), callback="parse_item", follow=True)
    )

    def __Init__(self, *args, **kwargs):
        domain = kwargs.pop("domain", '')
        self.allowed_mains = filter(None, domain.split(','))
        super(MyCrawler, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        return {
            "question_author": response.url,
        }