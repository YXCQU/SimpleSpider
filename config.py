# coding:utf-8

import random
from Downloader import UserAgents

# 通用headers
tyc_headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36",
    "Host": "m.tianyancha.com",
    "Referer": "https://m.tianyancha.com/search?key="
}
# 拉勾网headers
lagou_headers = {
    "User-Agent": random.choice(UserAgents.USER_AGENTS),
    "DNT": "1",
    "Host": "www.lagou.com",
    "Origin": "https://www.lagou.com",
    "Referer": "https://www.lagou.com/jobs/list_",
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": None,
    "X-Requested-With": "XMLHttpRequest"  # 请求方式XHR
}

# 微博headers
weibo_headers = {
    'User-agent': random.choice(UserAgents.USER_AGENTS),
    'Host': 'm.weibo.cn',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://m.weibo.cn/status/',
    'DNT': '1',
    'Connection': 'keep-alive',
}

# 头条headers
toutiao_headers = {
    'User-agent': random.choice(UserAgents.USER_AGENTS),
    'Host': 'www.toutiao.com',
    'Accept': 'application/json, text/javascript',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.toutiao.com/ch/news_hot/',
    'DNT': '1',
    'Connection': 'keep-alive',
}


# 通用请求头
def get_header():
    return {
        'User-Agent': random.choice(UserAgents.USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
    }


# 每次请求的最大超时时间
TIME_OUT = 8

# 请求重试次数
RETRY_TIME = 3

# 设置请求的间隔时间
WAIT_TIME = 1

# 最大并发数
MAX_DOWNLOAD_CONCURRENT = 3

# 最大线程数
MAX_DOWNLOAD_PROCESS = 2

# 队列容量
TASK_QUEUE_SIZE = 50

# 数据库配置
MONGO_URL = '127.0.0.1'
MONGO_DB = 'toutiao'
MONGO_DB_TAOBAO = 'taobao'
MONGO_TABLE = 'toutiao'
MONGO_TABLE_TAOBAO = 'toutiao'

GROUP_START = 1
GROUP_END = 20
KEYWORD = '街拍'
