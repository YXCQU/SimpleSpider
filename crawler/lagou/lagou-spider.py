import requests
import json
import time
from proxy import ip_proxy


ajax_url = 'https://www.lagou.com/jobs/positionAjax.json'

proxy = ip_proxy.get_proxy()

wait_time = 2


def get_content(post_param):
    # 使用post方式，data里面存放我们的参数，可以通过浏览器调试工具获得
    global wait_time
    time.sleep(wait_time)
    global proxy
    while True:
        try:
            r = requests.post(ajax_url, headers=headers, data=post_param, timeout=3,
                              proxies=proxy)
            # 使用代理访问
            result = json.loads(r.text)
            if result['success']:
                for item in result["content"]["positionResult"]["result"]:
                    print(item)
                wait_time = 2
                return result["content"]["positionResult"]["result"]
            else:
                print(result)
                proxy = ip_proxy.get_proxy()
                continue
        except Exception:
            print("IP不可用 %s" % proxy['http'])
            res = ip_proxy.del_proxy(proxy['http'].split(":")[0])
            print("已删除 %s" % res)
            proxy = ip_proxy.get_proxy()
            continue


# first 设置为False，我们用pn来翻页，pn：表示第几页，kd：表示搜索关键字
for i in range(1, 31):
    post_param = {"first": "false", "pn": i, "kd": " "}
    print("这是第 %d" % i + " 页")
    # time.sleep(2)
    get_content(post_param)
