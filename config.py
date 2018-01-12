# coding:utf-8

import random
import UserAgents

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
    # 'Cookie': 'SUB=_2A253O13yDeRhGeNK61AY8CzJwzyIHXVUxGO6rDV6PUNbktANLXP2kW1NSW85ShwUa0Be7OiaGwPQzEGsYs03NJMr',
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
    # 'Cookie': '__tasessionId=4do2m93l01515224454646; tt_webid=6507839417855657486; uuid="w:da936644313f4a9385784dea4eac2f0b"; UM_distinctid=160ca6a571e669-0a088d7ef4d7dd-61131b7e-1fa400-160ca6a571f84c; CNZZDATA1259612802=2023777230-1515221049-%7C1515221049',
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
