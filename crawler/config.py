# coding:utf-8

import random
from crawler import UserAgent_config

# 拉勾网headers
lagou_headers = {
    "User-Agent": random.choice(UserAgent_config.USER_AGENTS),
    "DNT": "1",
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Referer": "https://www.lagou.com/jobs/list_",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": None,
    "X-Requested-With": "XMLHttpRequest"  # 请求方式XHR
}


# 通用请求头
def get_header():
    return {
        'User-Agent': random.choice(UserAgent_config.USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
    }
