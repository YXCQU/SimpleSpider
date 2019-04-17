# coding:utf-8

import random
from download import UserAgents

######################
# 通用配置文件 config #
######################

# 米扑代理headers
mp_headers = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'origin': "https://proxy.mimvp.com",
    'referer': "https://proxy.mimvp.com/usercenter/regist.php",
    'cookie': "PHPSESSID=h6ut1onot32prn5ckh4s8aekoc",
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
}

# 天眼查headers
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


# 每次请求的最长超时时间
TIME_OUT = 15

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

# 代理网站配置信息
# 米扑代理 免费试用5小时
# 订单号、IP获取API
mp_url = 'https://proxyapi.mimvp.com/api/fetchopen.php?orderid={}&num=20&http_type=2,4,5&anonymous=3,' \
         '5&ping_time=5&transfer_time=10&check_success_count=100&filter_hour=1&result_fields=1,2,10,4,5,6,7,8,' \
         '9&result_format=json'
# 注册、验证码、用户订单信息 API
reg_url = 'https://proxy.mimvp.com/lib/user_regist_check.php'
code_url = 'https://proxy.mimvp.com/common/ygrcode.php?rand=0.09437166077013948'
user_info = 'https://proxy.mimvp.com/usercenter/userinfo.php'
