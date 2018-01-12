import requests
import json
import time
from config import get_header
from bs4 import BeautifulSoup

url = ''  # 你的付费连接
free_url = "https://proxy.mimvp.com/free.php"  # free url
free_params = ['in_hp', 'in_socks', 'out_socks']


# 付费米扑代理
def get_mimvp():
    """
    从接口获得代理IP
    :return:
    """
    time.sleep(2)
    try:
        r = requests.get(url, timeout=5)
    except:
        print("代理服务器问题")
    res = json.loads(r.text)
    with open('all_ip.json', 'a') as f:
        json.dump(res['result'], f)
        f.write(', \n')
    all_ip = res['result']
    tmp = {
        "HTTP": [],
        "HTTPS": [],
        "HTTP/HTTPS": [],
        "Socks4/Socks5": [],
        "Socks4": [],
        "Socks5": []
    }
    for ip in all_ip:
        # print(ip['ip:port'] + ip['http_type'])
        tmp[ip['http_type']].append(ip['ip:port'])
    # print(tmp)
    return tmp


# 付费版
def get_proxy():
    """
    获得代理list
    :return:list
    """
    proxy = get_mimvp()
    proxy_list = []

    if proxy['HTTP']:
        for ip in proxy['HTTP']:
            proxy_list.append({
                "http": "http://{}".format(ip)
            })
    if proxy["HTTPS"]:
        for ip in proxy['HTTPS']:
            proxy_list.append({
                "https": "http://{}".format(ip)
            })
    if proxy["HTTP/HTTPS"]:
        for ip in proxy['HTTP/HTTPS']:
            proxy_list.append({
                "http": "http://{}".format(ip),
                "https": "http://{}".format(ip)
            })
    if proxy["Socks4/Socks5"]:
        for ip in proxy['Socks4/Socks5']:
            proxy_list.append({
                "http": "socks5://{}".format(ip),
                "https": "socks5://{}".format(ip)
            })
    if proxy["Socks4"]:
        for ip in proxy['Socks4']:
            proxy_list.append({
                "http": "socks4://{}".format(ip),
                "https": "socks4://{}".format(ip)
            })
    if proxy["Socks5"]:
        for ip in proxy['Socks5']:
            proxy_list.append({
                "http": "socks5://{}".format(ip),
                "https": "socks5://{}".format(ip)
            })
    return proxy_list


# 免费代理
def get_free():
    r_http = requests.get(free_url, params={'proxy': free_params[0]}, headers=get_header())
    # r_socks1 = requests.get(free_url, params={'proxy': free_params[1]}, headers=get_header())
    # r_socks2 = requests.get(free_url, params={'proxy': free_params[2]}, headers=get_header())
    parse_free(r_http.text)

def parse_free(html):
    soup = BeautifulSoup(html, 'lxml')
    r = soup.select('tbody')[0]
    ips = r.select('.tbl-proxy-ip')
    ports = r.select('.tbl-proxy-port img')
    types = r.select('.tbl-proxy-type')
    for i in range(len(ips)):
        ip = ips[i].get_text()
        port = ports[i].attrs['src']
        ip_type = types[i].get_text()

    print(r)
    pass





if __name__ == '__main__':
    # res = get_proxy()
    # print(res)
    get_free()
