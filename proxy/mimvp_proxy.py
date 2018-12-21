import requests
from config import get_header
from bs4 import BeautifulSoup

# 订单号可以免费注册获得
order_id = '862000891125217287'
# url_https = f'https://proxyapi.mimvp.com/api/fetchopen.php?orderid={order_id}&num=20&anonymous=3,5&ping_time=5&transfer_time=10&check_success_count=100&result_fields=1,2,5,6,7,8&result_format=json'
# url_https = f'https://proxyapi.mimvp.com/api/fetchsecret.php?orderid={order_id}&num=5&result_fields=1,2,3&result_format=json'
url_https = f'https://proxyapi.mimvp.com/api/fetchopen.php?orderid={order_id}&num=20&result_fields=1,2&result_format=json&ping_time=5&transfer_time=10'


# 付费米扑代理
def get_mp_http(_url=None):
    """
    从接口获得代理IP
    :return:
    """
    try:
        r = requests.get(_url, timeout=8)
    except TimeoutError:
        print("代理服务器超时")
    res = r.json()
    all_ip = res['result']
    print(all_ip)

    for _ip in all_ip:
        ip = ''
        if 'HTTP' in _ip['http_type']:
            ip = 'http://' + _ip['ip:port']
        elif 'Socks4' in _ip['http_type']:
            ip = 'Socks4://' + _ip['ip:port']
        elif 'Socks5' in _ip['http_type']:
            ip = 'socks5://' + _ip['ip:port']
        yield ip


def proxy(func=None, url=None):
    """
    格式化 ip 为 requests 格式
    :param func:
    :param url:
    :return:
    """

    for ip in func(url):
        requests_template = {
            "https": "",
            "http": ""
        }
        if "http" in ip:
            requests_template['https'] = ip
            requests_template['http'] = ip
        elif "socks4" in ip:
            requests_template['https'] = ip
            requests_template['http'] = ip
        elif "socks5" in ip:
            requests_template['https'] = ip
            requests_template['http'] = ip
        yield requests_template


def get_proxy():
    return proxy(get_mp_http, url_https)


if __name__ == '__main__':
    # res = get_proxy()
    # print(res)
    for proxy in proxy(get_mp_http, url_https):
        print(proxy)
