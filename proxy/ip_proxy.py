import requests
import random
import json


def get_ip():
    """
    获得所有IP
    :return: 随机返回一个
    """
    r = requests.get('http://192.168.1.195:8010/')
    all_ip = json.loads(r.text)
    # print("总IP数量：%d" % len(all_ip))
    index = random.randint(0, len(all_ip) - 1)
    # print("这是第 %d" % str(index) + "个IP")
    ip = all_ip[index][0]
    port = all_ip[index][1]
    return ip, port


def get_proxy():
    """
    通过get_ip()获得ip，拼接为代理返回
    :return:
    """
    ip = get_ip()
    proxies = {
        'http': '%s:%s' % ip,
        'https': '%s:%s' % ip
    }
    return proxies


def del_proxy(ip):
    """
    删除不可用
    :param ip:
    :return:
    """
    ip = ip.split(":")[0]
    r = requests.get('http://192.168.1.195:8010/delete?ip=%s' % ip)
    return r.text


if __name__ == '__main__':
    """测试"""
    pass
