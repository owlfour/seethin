# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestBaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # image_urls是scrapy下载图片时自带的属性，不可以改变，如果要该成自定义的
    # 比如  URL=scrapy.Field()
    # 需要在settings文件中添加  IMAGES_URLS_FIELD='URL'  这个表示图片的url属性是URL
    image_urls = scrapy.Field()


