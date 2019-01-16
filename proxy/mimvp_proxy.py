import requests
import time
from config import mp_headers, mp_url, code_url, reg_url, user_info
from io import BytesIO
from qqai.vision.ocr import GeneralOCR
from util import ocr
import re


def get_mp_ip(url, types='json'):
    """
    获取米扑原始IP数据
    :param url:
    :param types: 返回数据类型，默认json格式
    :return:
    """
    try:
        r = requests.get(url, timeout=8)
    except Exception as e:
        print(e)
        return
    if types == 'text':
        return r.text
    return r.json()


def get_order_id():
    # 获取米扑的order id
    data = {
        "user_email": str(int(time.time())) + '@qq.com',
        "user_pwd": 'password.',
        "user_mobile": '13688889999',
        "forurl": 'login.php',
        "user_rcode": 0
    }
    session = requests.Session()
    try:
        # 获取验证码
        req = session.get(url=code_url, headers=mp_headers)
        result = ocr.get_capture(req.content)
        data["user_rcode"] = result['code'].lower()

        # 注册账号
        response = session.post(url=reg_url, headers=mp_headers, data=data)
        session.cookies.update(response.cookies)
        response = session.get(url=user_info)
        order_id = re.search("orderid=(\d+)", response.text).group(1)
        print(order_id)
    except Exception as e:
        print(e)


def get_mp_http(_url=None):
    """
    对ip进行处理
    :return:
    """

    res = get_mp_ip(_url)
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
    进一步格式化 ip，转为 requests proxies 格式
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
    # 测试方法
    # 订单号可以免费注册获得
    order_id = '864030902901263100'  # 网站注册 免费获得
    url_https = f'https://proxyapi.mimvp.com/api/fetchopen.php?orderid={order_id}&num=200&anonymous=3,5&ping_time=5&' \
        f'transfer_time=10&check_success_count=100&result_fields=1,2,5,6,7,8&result_format=json'
    #
    # s = get_mp_ip(url=url_https, types='json')
    # print(s)
    cookie = get_order_id()
    print(cookie)
