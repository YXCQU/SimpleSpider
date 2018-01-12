import requests

ip = '106.39.179.118:80'
proxies = {
    "http": "http://%s" % ip,
    "https": "http://%s" % ip
}
sock_ip = ''
socks4 = {
    'http': 'socks4://181.113.28.150:1080',
    'https': 'socks4://181.113.28.150:1080'
}
test_url = 'https://httpbin.org/ip'
test_url1 = 'http://ip.chinaz.com/getip.aspx'
r = requests.get(test_url1, proxies=socks4, timeout=10)  # https://httpbin.org/ip
r.encoding = 'utf-8'
print(r.text)
