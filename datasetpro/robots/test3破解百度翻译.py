import json

import  requests
if __name__ =="__main__":
    post_url='https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
    }
    data ={
        'kw':'dog'
    }
    response =requests.post(url=post_url,data=data,headers=headers)
    dic_obj=response.json()
    fp=open('./dog.json','w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
