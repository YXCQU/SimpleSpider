import requests
import json

"""
手机版拉钩爬取
"""
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Mobile Safari/537.36",
    "DNT": "1",
    "Host": "m.lagou.com",
    "Referer": "https://m.lagou.com/search.html",
    "X-Requested-With": "XMLHttpRequest"  # 请求方式XHR
}

params = {
    'city': '全国',
    'positionName': '',
    'pageNo': 1000,
    'pageSize': '15'
}

m_url = 'https://m.lagou.com/search.json'

index = 1
while True:
    params.update({'pageNo': index})
    r = requests.get(m_url, headers=headers, params=params)
    result = json.loads(r.text)
    with open('resul.txt', 'w') as f:
        json.dump(result, f)

    for item in result['content']['data']['page']['result']:
        print(item)
    import time
    time.sleep(5)
    index += 1
