import requests
import json

# 这里的header和上面的不同，大家试试看删掉一些还能不能获取数据
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "DNT": "1",
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Referer": "https://www.lagou.com/jobs/list_",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": None,
    "X-Requested-With": "XMLHttpRequest" # 请求方式XHR
}

ajax_url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&needAddtionalResult=false&isSchoolJob=0'

# first 设置为False，我们用pn来翻页，pn：表示第几页，kd：表示搜索关键字
post_param = {"first": "false", "pn": "179", "kd": "项目经理"}

# 使用post方式，data里面存放我们的参数，可以通过浏览器调试工具获得
r = requests.post(ajax_url, headers=headers, data=post_param)

result = json.loads(r.text)
try:
    for item in result["content"]["positionResult"]["result"]:
        print(item)
    print(result["content"]["positionResult"]["totalCount"])
except:
    print(result)