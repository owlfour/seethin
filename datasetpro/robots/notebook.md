# Day1

## 爬虫：

通过编写程序模拟浏览器上网抓取数据的过程

价值：

+ 数据银行

爬虫学的好监狱进的早 ：

+ 法律中不禁止
+ 具有违法风险
+ 善意爬虫  恶意爬虫

## 初始探入：

### 分类：

+ 通用爬虫   ：抓取系统重要的组成部分，抓取的是一整张页面数据

+ 聚焦爬虫：   建立通用爬虫的基础上，抓取页面的特定局部内容

+ 增量式爬虫：检测网站中数据更新的情况

  

### 矛与盾：

+ 反爬机制：
+ 反反爬策略：  UA伪装

### robots.txt协议：

规定了网站哪些数据可以被爬取

### http协议：

服务器和客户端进行数据交互的一种形式

常用请求头信息：  

-User-Agent               表示请求载体的身份标识

-Connecttion              表示完毕后是断开连接还是保持连接

常用响应头信息

-Content-Type           服务器响应回客户端数据类型

https协议 ：安全的超文本传输协议   证书秘钥加密

加密方式：

+ 对称秘钥加密
+ 非对称秘钥加密
+ 证书秘钥加密

# Day2:

## requests模块：

有两个模块 urllib 和requests模块

requests模块：python中原生的网络请求模块

作用：模块浏览器发请求

#### 如何使用：

使用流程

1.指定url

2.发起请求   get 或post

3.获取响应数据

4.持久化存储

# Day3：

聚焦爬虫：

使用流程

1.指定url

2.发起请求   get 和post

3.获取响应数据

4.数据解析

5.持久化存储

数据解析分类：

+ 正则
+ bs4    只能在python中
+ xpath(***)

数据解析原理概述：

解析的局部文件内容都会在标签之间或者标签对应的属性中进行存储

1.进行指定标签的定位

2.标签或者标签对应的属性中存储的数据值进行提取（解析）

text（字符串）content(二进制)  json(对象)



bs4数据解析原理：

1.实例化一个BeautifulSoup对象并且将页面源码数据加载到该对象中

2.通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取

环境 bs4 和 lxml

相关解析的方法和属性

soup.tagName      返回第一次出现的tagName(意思是标签)

soup.find('div')      返回第一次出现的div   属性定位

soup.find_all('div')  返回所有div

soup.select()         选择器可以是类可以是标签还可以是id   但是不支持索引定位

soup.tagName.text

soup.tagName.string          获取tagName只能是直系的文本内容

soup.tagName.get_text()    和text一样是获取某个标签的所有文本内容	

#### xpath解析：

最常用最便捷高效的解析方式 通用性

1、实例化一个etree对象 且需要将被解析的页面源码数据加载到改对象中

2、调用etree对象中的xpath方法结合着xpath表达实现标签的定位和内容的获取

环境：pip install lxml

实例化：

1、将本地的html文档源码加载到etree对象中 etree.parse(filepath)

2、互联网获取源码数据到改对象中     etree.HTML('page_text')

etree.xpath('/html//div')返回定位的text     /  表示一个层级   //表示多个层级    可以有属性定位    还可以有索引定位

取文本：

+ /text()    获取的标签中直系的文本内容
+ //text()  获取的是标签中非直系的文本内容

取属性：

+ /@attrName   attrName为标签名

# Day4:

## 验证码

反爬机制之一

如何识别：

+ 人工肉眼识别
+ 第三方自动识别   云打码

### 云打码

注册：用户和开发者都要注册

登录：普通用户登录

代理IP

代理IP类型：

http:

https:

代理IP的匿名度

+ 透明  服务器知道了该次请求使用了代理IP也知道真是IP
+ 匿名  知道了使用了代理  不知道真实IP
+ 高匿名  不知道使用了代理  也不知

http/https协议特性  ： 无状态

Cookie:用来让服务器端保留记录客户端相关状态

+ 手动处理：手动抓包 Cookie值  加载到headers
+ 自动处理：cookie是post请求后返回的

session会话对象：

作用：可以进行请求的发送 

​            若过程中产生了cookie则自动存储在session对象中

## 代理论

代理相关的网站：

快代理

西祠代理

www.goubanjia.com

# Day5:

### 高性能异步爬虫

方式：   

+ 多线程 多进程       好处：可以为相关阻塞操作单独开启线程或进程  弊端：无法无限制开启多线程进程

+ 线程池进程池        好处：可以减低系统对进程或者线程创建和销毁的频率，降低系统开销       弊端：池中线程或进程数量是有上限的

  from multiprocessing.dummy import Pool

  实例化线程池对象pool =Pool(4)

  pool.map(get_page,name_list)

  原则：线程池处理的是阻塞且耗时的操作

+ 单线程+异步协程

  event_ loop: 事件循环，相当于一个无限循环，我们可以把一些函数注册到这个事件循环上，当满足某些条件的时候，函数就会被循环执行。
  coroutine:协程对象，我们可以将协程对象注册到事件循环中，它会被事件循环调用。我们可以使用async关键字来定义一个方法，这个方法在调用时不会立即被执行，而是返回
  一个协程对象。
  task:任务，它是对协程对象的进一步封装， 包含了任务的各个状态。
  future:代表将来执行或还没有执行的任务，实际上和task 没有本质区别。
  async定义一个协程.
  await用来挂起阻塞方法的执行。

pip install aiohttp

# Day6:

### selenium模块

基于浏览器自动化的模块：

便捷获取网站中动态加载的数据

便捷实现模拟登录

环境： pip install selenium    下载浏览器驱动（驱动程序和浏览器映射）

实例化selenium对象:

from selenium import  webdriver

bro =webriver.Chrom(executable='./chromedriver')

对指定url发起请求

bro.get('http://'baidu.com)

获取浏览器当前页面页面数据

page_text = bro.page_source

解析

tree = etree.HTML(page_text) 

bro.quit()  #关闭浏览器

动作链：iframe





无头浏览器  无可视化界面  phantomjs停止维护

ChromeOptions  用来规避检测

验证码识别平台：超级鹰

# Day7:

### scragpy框架

框架：集成了很多功能并且具有很强**通用性**的项目**模板**

scrapy封装好的一个明星框架

功能：

+ 高性能的持久化存储
+ 异步的数据下载
+ 高性能的数据解析
+ 分布式

#### scrapy基本使用

安装环境： win10

+ pip install wheel
+ 下载twisted    [下载](http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted)
+ 安装twisted : pip install (你下载的对应文件名)Twisted-17.1.0-cp36m-win_amd64.whl
+ pip install pywin32
+ pip install scrapy

创建一个工程：

+ 1.scrapy startproject projectname
+ 2.cd projectname
+ 3.在spiders子目录中创建一个爬虫文件 scrapy genspider  spidersname www.xxx.com

执行工程：

+ scrapy crawl spidername

```py
#spidername.py文件
#-*- coding: utf-8 -*-
import scrapy

class FirstSpider(scrapy.Spider):
      name ='spidername'#爬虫文件的名称：就是爬虫文件的一个唯一标识
      allowed_domains=['www.xxx.com']#允许的域名：用来限定start_urls列表哪些url可以进行请求发送
      start_urls=['https://www.xxx.com/']#起始的url列表：该列表中存放的url会被scrapy自动进行的请求发送
      #爬虫的解析函数
      def parse (self,response):
          div_list = response.xpath('路径')
          #xpath()返回的是列表，但是列表元素一定是Selector类型的对象
          #extract()可以将Selector对象中data参数存储字符串取出来
          for div in div_list:
              
      
```

```py
#在settings.py中
#设置robotstxt协议
ROBOTSEXT_OBEY = False
#设置指定类型的日记信息
LOG_LEVEL ='ERROR'
#设置请求载体  会默认的一般不设置
USER_AGENT ='你的'
```

```py
#scrapy持久化存储
#1.基于终端指令：
   只可以将parse方法的返回值存储到本地文件中
   #类型可以为 json  jsonlines jl csv xml
   #指令： scrapy crawl xxx -o filePath
   #好处：简介高效便捷
   #缺点：局限性比较强
#2.基于管道
   #编码流程：数据解析->将解析的数据封装存储到item类型的对象中->将item类型的对象提交给管道进行持久化存储的操作->在管道类中的procees_item中要将其接受到的item对象中存储的数据进行持久化存储操作->在配置文件中开启管道
   #好处：通用性强
   #缺点：
```

``` py
#基于spider的全站数据爬取
```

#### 图片爬取

基于scrapy爬取字符串类型的数据和爬取图片类型的数据区别

+ 字符串：只需要基于xpath进行解析且提交管道进行持久化存储
+ 图片：xpath解析出图片src的属性值，单独的对图片地址发起请求获取图片二进制类型的数据

ImagesPipelIne:(图片管道):

只要将img的src的属性值进行解析，提交到管道，管道就会对图片的src进行请求发送获取图片的二进制数据

##### 使用流程：

1.数据解析（图片的地址）

2.将存储图片地址的item提交定制的管道类

3.在管道文件中自定制一个基于ImagesPipeLine的一个管道类

+ get_media_request
+ file_path
+ item_completed

4.在配置文件中：

+ 指定图片存储的目录：IMAGES_STORE='./imgs'
+ 指定开启的管道：自定制的管道类



[爬虫文档](https://book.apeland.cn/details/408/)

[scrapy官方文档](https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/overview.html)