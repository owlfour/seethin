
#UA伪装  将对应User_Agent封装到一个字典中

import requests

url = 'https://www.sogou.com/web/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}
kw = input('输入：')
param = {
    'query': kw
}
response = requests.get(url=url, param=param,headers=headers)  # 发起请求返回响应对象
page_text = response.text  # 返回字符串形式的响应数据
print(page_text)
filename = kw + '.html'
with open(filename, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print("爬取数据完毕")
