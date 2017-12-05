import requests
import random
import json


def get_ip():
    """
    获得所有IP
    :return: 随机返回一个
    """
    r = requests.get('http://111.230.144.236:5010/get/')
    # index = random.randint(0, len(all_ip) - 1)
    # ip = all_ip[index][0]
    # port = all_ip[index][1]
    return r.text


def get_all_ip():
    url = 'http://111.230.144.236:5010/get_all/'
    r = requests.get(url)
    return json.loads(r.text)


def get_proxy():
    """
    通过get_ip()获得ip，拼接为代理返回
    :return:
    """
    ip = get_ip()
    proxies = {
        'https': 'https://%s' % ip,
        'http': 'http://%s' % ip
    }
    return proxies


def del_ip(ip):
    r = requests.get("http://111.230.144.236:5010/delete/?proxy={}".format(ip))
    return r.text


def del_proxy(ip):
    """
    删除不可用
    :param ip:
    :return:
    """
    return del_ip(ip)


if __name__ == '__main__':
    """测试"""
    print(get_proxy())
    pass
