import requests
from config import *
from lxml import etree
import time

def get_money(key):
    url = 'https://www.tianyancha.com/search?key={}'
    r = requests.get(url.format(key), headers=tyc_headers)
    html = etree.HTML(r.text)
    result = html.xpath('//*[@id="web-content"]/div/div[1]/div/div[3]/div/div/div[2]/div[2]/div[2]/span/text()')[0]
    print(result)
    return result


if __name__ == '__main__':
    with open('excel1.txt', 'r') as f:
        for line in f.readlines():

            get_money('梁溪区瑞耀汽修服务部')
