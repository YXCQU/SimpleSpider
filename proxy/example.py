from proxy import ip_proxy
import requests

r = requests.get('http://httpbin.org/ip', proxies=ip_proxy.get_proxy(), timeout=4)
r.encoding = 'utf-8'
print(r.text)
