import re
import scrapy
from scrapy_splash import SplashRequest #重新定义了请求
import json


class DuduSpider(scrapy.Spider):
    name = 'dudu'
    allowed_domains = ['image.baidu.com']
    start_urls= ['https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E6%A6%B4%E8%8E%B2']

    # splash lua script
    lua_script = """
         function main(splash, args)
            local num_scrolls = 10  -- 翻页数
            local scroll_delay = 0.5  -- 翻页等待时间
            local scroll_to = splash:jsfunc("window.scrollTo")
            local get_body_height = splash:jsfunc(
                "function() {return document.body.scrollHeight;}"
            )
            assert(splash:go(args.url))
            splash:wait(args.wait)
            for _ = 1, num_scrolls do
                scroll_to(0, get_body_height())
                splash:wait(scroll_delay)
            end 
            return splash:html()
         end
         """
    #          splash:runjs("document.getElementsByClassName('mod_turn_page clearfix mt20')[0].scrollIntoView(true)")
    # mod_turn_page clearfix mt20 分页符标签，表示下拉到底部，从而解决异步加载。在返回渲染后的页面
    # Element.scrollIntoView() 方法让当前的元素滚动到浏览器窗口的可视区域内。

    def start_requests(self):  # 重新定义起始爬取点
        for url in self.start_urls:
           yield SplashRequest(url)
    def parse(self, response):
        print(response.json)

