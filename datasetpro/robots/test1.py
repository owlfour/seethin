#爬取搜狗首页数据
import  requests

if __name__ =="__main__":
    url = 'https://www.sogou.com/'
    response=requests.get(url=url)  #发起请求返回响应对象
    page_text=response.text     #返回字符串形式的响应数据
    print(page_text)
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取数据完毕")
