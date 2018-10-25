import requests
from config import *
from lxml import etree
import time
import json
import random


def get_money(key):
    ips = []
    with open('ip.txt', 'r') as f:
        ips = [i for i in f.readlines()]
    index = random.randint(0, len(ips) - 1)
    proxy = {
        'https': 'https://%s' % ips[index].replace('\n', ''),
        'http': 'http://%s' % ips[index].replace('\n', '')
    }
    url = 'https://www.tianyancha.com/search?key={}'
    try_num = 3
    while try_num > 0:
        try:
            r = requests.get(url.format(key), headers=tyc_headers, timeout=6)
            html = etree.HTML(r.text)
            # print(r.text)
            result = html.xpath('//*[@id="web-content"]/div/div[1]/div/div[3]/div/div/div[2]/div[2]/div[2]/span/text()')[0]
            print(result)
            return result
        except Exception as e:
            print(e)
            index = random.randint(0, len(ips) - 1)
            proxy = {
                'https': 'https://%s' % ips[index].replace('\n', ''),
                'http': 'http://%s' % ips[index].replace('\n', '')
            }
            try_num -= 1
            continue


if __name__ == '__main__':
    file_name = 'excel1.txt'
    with open(file_name, 'r') as f:
        for line in f.readlines():
            res = ' '
            try:
                res = get_money(line)
                if not res:
                    res = ' '
            except:
                res = ' '
            finally:
                with open('res_' + file_name, 'a') as f1:
                    f1.write(res)
                    f1.write('\n')
