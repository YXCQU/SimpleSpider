import requests
import time
from config import mp_headers, code_url, reg_url, user_info, TIME_OUT
from db.model import IPInfo
from util import ocr
import re


##
# 米扑代理
##
def get_mp_ip(url, types='json'):
    """
    获取米扑原始IP数据
    :param url:
    :param types: 返回数据类型，默认json格式
    :return:
    """
    try:
        r = requests.get(url, timeout=TIME_OUT)
    except Exception as e:
        print(e)
        return
    if types == 'text':
        return r.text
    return r.json()


def get_order_id():
    # 获取米扑代理的order id

    # post 数据格式
    data = {
        "user_email": str(int(time.time())) + '@gmail.com',
        "user_pwd": 'Pass.Word',
        "user_mobile": str(int(time.time())) + '7',
        "forurl": 'login.php',
        "user_rcode": 0
    }

    all_ip = IPInfo.select().order_by(IPInfo.id.desc())
    # 注册失败次数
    count = 0
    for _ip in all_ip:
        try:
            print("测试次数: " + str(count))
            # 获取验证码
            session = requests.Session()
            req = session.get(url=code_url, headers=mp_headers)
            result = ocr.get_capture(req.content)
            data["user_rcode"] = result['code'].lower()

            # 代理
            ip = _ip.ip_port
            ip_type = _ip.http_type
            proxy = {"https": f"http://{ip}", "http": f"http://{ip}"}
            if 'socks4' in ip_type:
                proxy = {"https": f"socks4://{ip}", "http": f"socks4://{ip}"}
            # 使用获得的代理尝试次数
            if count >= 7:
                proxy = None
                count = 0
            # 使用代理注册账号
            print(proxy)
            response = session.post(url=reg_url, headers=mp_headers, timeout=TIME_OUT, data=data, proxies=proxy)
            session.cookies.update(response.cookies)
            response = session.get(url=user_info)
            order_id = re.search(r"orderid=(\d+)", response.text).group(1)
            if int(order_id) > 99999:
                return order_id
        except:
            print('注册失败,重新注册中')
            count += 1
            continue


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
