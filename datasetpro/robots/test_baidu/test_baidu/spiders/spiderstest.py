
import scrapy
import  json
from  test_baidu.items import  TestBaiduItem

class SpiderstestSpider(scrapy.Spider):
    name = 'spiderstest'
    allowed_domains = ['image.baidu.com']
    #start_urls = ['https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E6%A6%B4%E8%8E%B2']

    # 重写start_urls，按照我们自己的需求
    def start_requests(self):
        for i in range(30, 120, 30):
            url = "https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E6%A6%B4%E8%8E%B2".format(
                i)
            # 交给调度器
            yield scrapy.Request(url, callback=self.parse)



    def parse(self, response):
        imgs = json.loads(response.body).get("data")  # json文件是一个字典
        # print(imgs),imgs是一个列表
        for img in imgs:
            item = TestBaiduItem()
            item['image_urls'] = [img['middleURL']]
            print(img['middleURL'])
            yield (item)



