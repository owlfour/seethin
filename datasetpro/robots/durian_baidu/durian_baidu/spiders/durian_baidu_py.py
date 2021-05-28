import scrapy


class DurianBaiduPySpider(scrapy.Spider):
    name = 'durian_baidu.py'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']
    #关键字列表
    search_lists=['榴莲','猪','durian']
    #关键字对应页数

    def parse(self, response):
        pass
