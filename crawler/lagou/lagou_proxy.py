from proxy import ip_proxy
import requests
import multiprocessing
import time


def del_ip(ip):
    r = requests.get("http://111.230.144.236:5010/delete/?proxy={}".format(ip))
    return r.text


def check_Proxy():
    time.sleep(1)
    all_ip = ip_proxy.get_all_ip()
    for ip in all_ip:
        proxies = {
            "http": "%s" % ip,
            "https": "%s" % ip
        }

        test_url = 'http://ip.chinaz.com/getip.aspx'
        try:
            r = requests.get(test_url, proxies=proxies, timeout=3)
            if 'address' in r.text:
                print(r.text)
            else:
                print(del_ip(ip))
        except:
            print(del_ip(ip))


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=check_Proxy)
    p1.start()
    print("start process p1")
    p1.join()
    print("end main process")
