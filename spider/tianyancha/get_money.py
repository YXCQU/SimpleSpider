import requests
from config import *
from lxml import etree
from proxy.mp import get_requests_proxy


def get_money(key, proxy=None):
    """
    获取公司的注册资金
    :param key:
    :param proxy:
    :return:
    """
    url = f'http://m.tianyancha.com/search?key={key}'
    try_num = 1
    while try_num > 0:
        try:
            print(proxy)
            r = requests.get(url, headers=tyc_headers, timeout=10, proxies=proxy)
            html = etree.HTML(r.text)
            # print(r.text)
            result = html.xpath('//div[@class="search_row_new_mobil"]/div[1]/div[2]/span')[0].text
            print(result)
            return result
        except Exception as e:
            print(e)
            try_num -= 1
            continue


if __name__ == '__main__':
    for p in get_requests_proxy():
        get_money('editorai', p)
