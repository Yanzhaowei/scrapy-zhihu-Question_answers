# scrapy-zhihu-Question_answers爬取知乎问答的所有问题，但是知乎的题主是默认隐藏的爬取不到，所以爬取的对象有，问题title, anser_author, anser_content
question_url,过滤content中的空行，

run
scrapy crawl zhihu就会爬取，存储在mysql,没有做分布式，咩有做模拟登陆，为了不被ban，自写userAgent.py,模拟网页访问
