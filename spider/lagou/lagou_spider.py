import requests
import json
import time
from config import *
import random
from proxy import mimvp_proxy
from lxml import etree

ajax_url = 'https://www.lagou.com/jobs/positionAjax.json'
wait_time = 2
proxies_list = []
proxies_list = mimvp_proxy.get_requests_proxy()


# local_ip = requests.get("http://ip.chinaz.com/getip.aspx", timeout=10).text


def get_from_list():
    global proxies_list
    if proxies_list.__len__() > 10:
        return proxies_list[0]
    else:
        proxies_list = mimvp_proxy.get_requests_proxy()
    return None


def del_from_list(proxy):
    global proxies_list
    if proxies_list.__len__() > 0:
        try:
            proxies_list.remove(proxy)
            return True
        except Exception as e:
            print(e)
    else:
        get_from_list()
    return True


def ip_cool_down(oldproxy):
    proxies_list.append(oldproxy)


proxy = get_from_list()


def get_content(post_param):
    # 使用post方式，data里面存放我们的参数，可以通过浏览器调试工具获得
    global wait_time
    time.sleep(wait_time)
    global proxy
    while True:
        try:
            r = requests.post(ajax_url, headers=lagou_headers, data=post_param, timeout=15, proxies=proxy)
            # r = requests.post(ajax_url, headers=config.lagou_headers, data=post_param, timeout=10)
            # 使用代理访问
            result = json.loads(r.text)
            sql_data = []
            if result['success']:
                for item in result["content"]["positionResult"]["result"]:
                    data = [item['companyId'], item['positionName'], item['workYear'], item['education'],
                            item['jobNature'],
                            item['positionId'], item['createTime'],
                            item['city'], item['industryField'], item['positionAdvantage'], item['salary'],
                            item['companySize'],
                            item['score'], item['companyFullName'], item['financeStage']]
                    sql_data.append(data)
                if sql_data:
                    # DAO.mysql_insert(sql_data)
                    print(sql_data)
                wait_time = 5
                return result["content"]["positionResult"]["result"]
            else:
                print(result)
                # now_ip = requests.get("http://ip.chinaz.com/getip.aspx", proxies=proxy, timeout=10).text
                # if result['clientIp'] in now_ip:
                #     ip_cool_down(proxy)
                # elif result['clientIp'] in local_ip:
                del_from_list(proxy)
                print('删除当前代理')
                proxy = get_from_list()
                time.sleep(2)
                continue
        except Exception as e:
            print(e)
            rb = del_from_list(proxy)
            print("出错删除当前代理 %s" % rb)
            proxy = get_from_list()
            continue


def get_money(key):
    proxy1 = get_from_list()
    url = 'https://www.tianyancha.com/search?key={}'
    try_num = 4
    while try_num > 0:
        try:
            r = requests.get(url.format(key), headers=tyc_headers, proxies=proxy1, timeout=6)
            html = etree.HTML(r.text)
            result = html.xpath('//*[@id="web-content"]/div/div[1]/div/div[3]/div/div/div[2]/div[2]/div[2]/span/text()')[0]
            print(result)
            return result
        except Exception as e:
            print(e)
            del_from_list(proxy1)
            proxy1 = get_from_list()
            try_num -= 1
            continue


if __name__ == '__main__':
    # first 设置为False，我们用pn来翻页，pn：表示第几页，kd：表示搜索关键字
    # i = 1
    # position_params = ['', 'java', 'PHP', 'C++', 'Android', 'Javascript', 'iOS', 'Python', 'UI设计师',
    #                    '产品总监', '产品经理', 'html5', '深度学习', '机器学习', '自然语言处理']
    # for kd in position_params:
    #     while True:
    #         print(kd + ' 第 %s' % i + ' 页')
    #         post_param = {"first": "false", "pn": i, "kd": kd}
    #         res = get_content(post_param)
    #         if len(res) == 0:
    #             i = 1
    #             break
    #         i += 1
    # print(proxy)
    file_name = 'excel1.txt'
    with open(file_name, 'r') as f:
        for line in f.readlines():
            res = ' '
            try:
                res = get_money(line)
            except:
                res = ' '
            with open('res_' + file_name, 'a') as f1:
                f1.write(res)
                f1.write('\n')
