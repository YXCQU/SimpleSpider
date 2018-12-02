# coding:utf-8

import random
import UserAgents

# 通用headers
tyc_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
    "DNT": "1",
    "Host": "www.tianyancha.com",
    "Referer": "https://www.tianyancha.com/search?key=",
    "Cookie": "aliyungf_tc=AQAAAOhregsZmQ4AYD2ktGTq0XGoFoGQ; csrfToken=24us384OjrbLoMvkC1A5Ur4u; TYCID=0893e3b0d77711e8a3d2b56d1f28ed41; undefined=0893e3b0d77711e8a3d2b56d1f28ed41; ssuid=4879515534; _ga=GA1.2.785143276.1540376725; _gid=GA1.2.323982156.1540376725; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1540376724,1540378368,1540388766,1540388797; token=bf22bd9f62024b9e8a95a0e1c690e562; _utm=863b9180383c49d5b2d2ee6484ac9d51; tyc-user-info=%257B%2522myQuestionCount%2522%253A%25220%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A0%252C%2522vipManager%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg3NTI5OTU5NyIsImlhdCI6MTU0MDM5MTQ0OSwiZXhwIjoxNTU1OTQzNDQ5fQ.arHGF04_F-fZNyaPGoOPmfddSD73_KKbPEbCOIr1hYFus0PjhPACgiY8e7kxIsksn5g4coGV0bKC3VJlILu7ZA%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218875299597%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg3NTI5OTU5NyIsImlhdCI6MTU0MDM5MTQ0OSwiZXhwIjoxNTU1OTQzNDQ5fQ.arHGF04_F-fZNyaPGoOPmfddSD73_KKbPEbCOIr1hYFus0PjhPACgiY8e7kxIsksn5g4coGV0bKC3VJlILu7ZA; _gat_gtag_UA_123487620_1=1; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1540391895"
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
