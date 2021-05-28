import scrapy


class Spiderstest1Spider(scrapy.Spider):
    name = 'spiderstest1'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
