import requests
import json
import time

url = 'https://proxy.mimvp.com/api/fetch.php?orderid=860171205093855810&num=100&result_fields=1,2&result_format=json'


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


if __name__ == '__main__':
    res = get_proxy()
    print(res)
