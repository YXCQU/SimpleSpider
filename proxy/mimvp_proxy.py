import requests
from bs4 import BeautifulSoup

# 订单号可以免费注册获得
order_id = '866030702906124109'  # 864000460225100593
url_https = f'https://proxyapi.mimvp.com/api/fetchopen.php?orderid={order_id}&num=200&anonymous=3,5&ping_time=5&transfer_time=10&check_success_count=100&result_fields=1,2,5,6,7,8&result_format=json'


# url_https = f'https://proxyapi.mimvp.com/api/fetchsecret.php?orderid={order_id}&num=20&result_fields=1,2,3&result_format=json'
# url_https = f'https://proxyapi.mimvp.com/api/fetchopen.php?orderid={order_id}&num=20&result_fields=1,2&result_format=json&ping_time=5&transfer_time=10'


def get_mp(url, types='json'):
    """
    获取米扑原始IP数据
    :param url:
    :param types:
    :return:
    """
    try:
        r = requests.get(url, timeout=8)
    except TimeoutError:
        print("代理服务器超时")
        return
    if types == 'text':
        return r.text
    return r.json()


# 付费米扑代理
def get_mp_http(_url=None):
    """
    初步处理 IP
    :return:
    """

    res = get_mp(_url)
    all_ip = res['result']

    for _ip in all_ip:
        ip = ''
        if 'HTTP' in _ip['http_type']:
            ip = 'http://' + _ip['ip:port']
        elif 'Socks4' in _ip['http_type']:
            ip = 'Socks4://' + _ip['ip:port']
        elif 'Socks5' in _ip['http_type']:
            ip = 'socks5://' + _ip['ip:port']
        yield ip


def requests_proxy(func=None, url=None):
    """
    格式化 ip 为 requests proxy格式
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


def get_requests_proxy():
    return requests_proxy(get_mp_http, url_https)


if __name__ == '__main__':
    # 打印显示
    for proxy in requests_proxy(get_mp_http, url_https):
        print(proxy)
