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
s = [{'check_total_count': 458, 'check_success_ratio': 0.90393013100437, 'transfer_time': 6.910299,
      'ping_time': 0.272551, 'check_success_count': 414, 'ip:port': '64.15.69.126:8080', 'http_type': 'HTTPS',
      'country': '加拿大'}, {'check_total_count': 248, 'check_success_ratio': 0.85887096774194, 'transfer_time': 4.358121,
                          'ping_time': 0.236662, 'check_success_count': 213, 'ip:port': '124.81.123.2:8080',
                          'http_type': 'HTTPS', 'country': 'null'},
     {'check_total_count': 390, 'check_success_ratio': 0.98717948717949, 'transfer_time': 0.189521,
      'ping_time': 0.028821, 'check_success_count': 385, 'ip:port': '124.74.111.190:8888', 'http_type': 'Socks4',
      'country': '中国:上海'},
     {'check_total_count': 144, 'check_success_ratio': 0.89583333333333, 'transfer_time': 2.711986,
      'ping_time': 0.500929, 'check_success_count': 129, 'ip:port': '138.97.236.11:1080', 'http_type': 'Socks4',
      'country': '阿根廷'}, {'check_total_count': 440, 'check_success_ratio': 0.82045454545455, 'transfer_time': 0.285509,
                          'ping_time': 0.038678, 'check_success_count': 361, 'ip:port': '118.122.92.252:37801',
                          'http_type': 'Socks4/Socks5', 'country': '中国:四川'},
     {'check_total_count': 652, 'check_success_ratio': 0.99233128834356, 'transfer_time': 4.43855, 'ping_time': 0.23136,
      'check_success_count': 647, 'ip:port': '201.150.255.185:3128', 'http_type': 'HTTPS', 'country': '墨西哥'},
     {'check_total_count': 246, 'check_success_ratio': 0.97560975609756, 'transfer_time': 2.168281,
      'ping_time': 0.234421, 'check_success_count': 240, 'ip:port': '109.197.184.50:8080', 'http_type': 'HTTPS',
      'country': '波兰'}, {'check_total_count': 402, 'check_success_ratio': 0.98258706467662, 'transfer_time': 1.854528,
                         'ping_time': 0.339218, 'check_success_count': 395, 'ip:port': '117.102.224.10:1080',
                         'http_type': 'Socks4', 'country': '印度'},
     {'check_total_count': 365, 'check_success_ratio': 0.98356164383562, 'transfer_time': 1.522966,
      'ping_time': 0.179377, 'check_success_count': 359, 'ip:port': '148.251.238.35:8080', 'http_type': 'HTTPS',
      'country': '德国'}, {'check_total_count': 350, 'check_success_ratio': 0.95714285714286, 'transfer_time': 0.105357,
                         'ping_time': 0.016056, 'check_success_count': 335, 'ip:port': '223.241.214.44:1217',
                         'http_type': 'Socks4/Socks5', 'country': '中国:安徽'},
     {'check_total_count': 388, 'check_success_ratio': 0.99484536082474, 'transfer_time': 1.861269,
      'ping_time': 0.327256, 'check_success_count': 386, 'ip:port': '176.37.169.117:1080', 'http_type': 'Socks4',
      'country': '乌克兰'}, {'check_total_count': 480, 'check_success_ratio': 0.97916666666667, 'transfer_time': 1.658752,
                          'ping_time': 0.315066, 'check_success_count': 470, 'ip:port': '103.54.148.50:1080',
                          'http_type': 'Socks4', 'country': '孟加拉国'},
     {'check_total_count': 117, 'check_success_ratio': 0.88888888888889, 'transfer_time': 1.56848,
      'ping_time': 0.150053, 'check_success_count': 104, 'ip:port': '47.89.37.177:3128', 'http_type': 'HTTPS',
      'country': '中国:香港'},
     {'check_total_count': 463, 'check_success_ratio': 0.98920086393089, 'transfer_time': 1.147217,
      'ping_time': 0.226444, 'check_success_count': 458, 'ip:port': '103.54.148.54:1080', 'http_type': 'Socks4',
      'country': '孟加拉国'}, {'check_total_count': 335, 'check_success_ratio': 0.95820895522388, 'transfer_time': 1.233008,
                           'ping_time': 0.236129, 'check_success_count': 321, 'ip:port': '109.238.208.43:1080',
                           'http_type': 'Socks4', 'country': '捷克'},
     {'check_total_count': 540, 'check_success_ratio': 0.84444444444444, 'transfer_time': 7.461642,
      'ping_time': 0.304464, 'check_success_count': 456, 'ip:port': '43.250.81.141:8080', 'http_type': 'HTTPS',
      'country': '孟加拉'},
     {'check_total_count': 752, 'check_success_ratio': 0.9375, 'transfer_time': 5.383063, 'ping_time': 0.224285,
      'check_success_count': 705, 'ip:port': '217.30.64.26:53281', 'http_type': 'HTTPS', 'country': '捷克'},
     {'check_total_count': 238, 'check_success_ratio': 0.94117647058824, 'transfer_time': 0.753935,
      'ping_time': 0.14262, 'check_success_count': 224, 'ip:port': '31.220.183.217:53356', 'http_type': 'Socks4',
      'country': '俄罗斯'}, {'check_total_count': 189, 'check_success_ratio': 0.98412698412698, 'transfer_time': 7.731225,
                          'ping_time': 0.204463, 'check_success_count': 186, 'ip:port': '213.155.250.46:3128',
                          'http_type': 'HTTPS', 'country': '捷克'},
     {'check_total_count': 250, 'check_success_ratio': 0.932, 'transfer_time': 2.436061, 'ping_time': 0.267933,
      'check_success_count': 233, 'ip:port': '202.182.57.10:8080', 'http_type': 'HTTPS', 'country': '印度'}]
