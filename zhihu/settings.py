# -*- coding: utf-8 -*-
# Scrapy settings for zhihu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html


BOT_NAME = 'zhihu'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

# 禁止cookies,防止被ban
# COOKIES_ENABLED = False

# 取消默认的useragent 使用新的useragent
DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'zhihu.rotate_useagent.RotateUserAgentMiddleware' :300
}

ITEM_PIPELINES = {
    # 'zhihu.pipelines.ZhihuPipeline':300,        # 保存文件
    'zhihu.pipelines.MysqlStorePipeline':300,   # 保存数据库
    'scrapy_redis.pipelines.RedisPipeline': 400,   # 设置redis
}

# mysql
MYSQL_HOST = "101.201.141.232"
MYSQL_DBNAME = "crawlingData"
MYSQL_USER = "crawling"
MYSQL_PASSWD = "crawling@123"

LOG_LEVEL = 'DEBUG'
# redis config
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 不清理redisqueue,允许暂停和重启crawls
SCHEDULER_PERSIST = True
# 过滤重复URL
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
DUPEFILTER_DEBUG = True
# Schedule requests using a priority queue. (default)
# 其实有三种： FIFO 的spiderqueue,LIFI的spiderstack
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
# 该项仅对queueclass is SpiderQueue or SpiderStack生效，阻止spider被关闭的最大空闲时间
SCHEDULER_IDLE_BEFORE_CLOSE= 10
# 链接redis
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379