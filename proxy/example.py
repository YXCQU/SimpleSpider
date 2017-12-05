import requests

ip = '182.23.58.188:8080'
proxies = {
    "http": "http://%s" % ip,
    "https": "http://%s" % ip
}
sock_ip = ''
socks4 = {
    'http': 'socks4://58.241.32.186:1080',
    'https': 'socks4://58.241.32.186:1080'
}
test_url = 'https://httpbin.org/ip'
test_url1 = 'http://ip.chinaz.com/getip.aspx'
r = requests.get(test_url1, proxies=socks4, timeout=15, )  # https://httpbin.org/ip
r.encoding = 'utf-8'
print(r.text)
