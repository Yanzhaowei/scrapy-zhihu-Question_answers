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
COOKIES_ENABLED = False

DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'zhihu.rotate_useagent.RotateUserAgentMiddleware' :400
}

ITEM_PIPELINES = {
    # 'zhihu.pipelines.ZhihuPipeline':300,        # 保存文件
    'zhihu.pipelines.MysqlStorePipeline':300    # 保存数据库
}

# 数据库设置
MYSQL_HOST = '101.201.141.232'
MYSQL_DBNAME = 'crawlingData'       #数据库名字
MYSQL_USER = 'crawling'             #数据库账号
MYSQL_PASSWD = 'crawling@123'       #数据库密码
