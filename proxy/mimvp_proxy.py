import requests
from config import get_header
from bs4 import BeautifulSoup

order_id = '861080148271221207'
url = f'https://proxyapi.mimvp.com/api/fetchsecret.php?orderid={order_id}&num=5&http_type=3&result_fields=1,2,3'
s = 'https://proxyapi.mimvp.com/api/fetchopen.php?orderid=861080148271221207&num=20&http_type=2&ping_time=1&transfer_time=5&check_success_count=100&filter_hour=12&result_fields=1,2&result_format=json'
free_url = "https://proxy.mimvp.com/free.php"  # free url
free_params = ['in_hp', 'in_socks', 'out_socks']


# 付费米扑代理
def get_mimvp():
    """
    从接口获得代理IP
    :return:
    """
    try:
        r = requests.get(url, timeout=8)
    except TimeoutError:
        print("代理服务器超时")
    res = r.json()
    all_ip = res['result']

    for ip in all_ip:
        yield ip['ip:port']


if __name__ == '__main__':
    # res = get_proxy()
    # print(res)
    get_mimvp()
