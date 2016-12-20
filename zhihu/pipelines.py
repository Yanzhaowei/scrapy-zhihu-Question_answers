# -*- coding: utf-8 -*-
import codecs
import os
import json
import redis
import MySQLdb
import MySQLdb.cursors
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

'''
class ZhihuPipeline(object):
    def process_item(self, item, spider):
        item["crawled"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        item["spider"] = spider.name
        os.makedirs('data/' + item['question_title'])
        file = codecs.open('data/' + item['question_title'] + "//" + item['question_title'] + '.json', 'wb',
                           encoding='utf-8')
        line = json.dumps(dict(item)) + "\n"
        file.write(line.decode("unicode_escape"))
        return item
'''
class MysqlStorePipeline(object):
        # 插入数据库
        # pipeline 默认调用
        def process_item(self,spider):
            r = redis.StrictRedis(host='127.0.0.1', port=6379)
            conn = MySQLdb.connect(host="101.201.141.232", user="crawling", passwd="crawling@123", db="crawlingData", charset="utf8")
            while True:
                source, data = r.blpop(["zhihu:items"])
                item = json.loads(data)
                # 当前时间
                now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

                param_author_content = '\'' + json.dumps(item["author_content"], ensure_ascii=False) + '\''
                param_question_type = '\'' + json.dumps(item["question_type"], ensure_ascii=False) + '\''
                params = (
                    item["question_title"],
                    param_author_content,
                    item["question_author"],
                    param_question_type,
                    item["question_url"], now)

                try:
                    cur = conn.cursor()
                    sql = "insert into t_QA_Data(qus, ans, qus_persion, type, source_url, time) values(%s, %s, %s, %s, %s, %s)"
                    cur.execute(sql, params)
                    conn.commit()
                    cur.close()
                    return item
                except MySQLdb.Error,e:
                    print "MysqlDb error %d: %s" % (e.args[0], e.args[1])


