import requests
import json
from config import *

# 爬取今日头条
api_url = 'https://www.toutiao.com/api/pc/feed/'


def get_news_hot():
    params = {
        'category': 'news_hot',
        'utm_source': 'toutiao',
        'widen': 1,
        'max_behot_time': 0,
        'max_behot_time_tmp': 0,
        'tadrequire': True,
        # 'as': 'A195CA658009AF9',
        # 'cp': '5A50399ADF29AE1',
        # '_ignature': 'v7eWdgAA5fTUJxFJ7t99gb - 3lm'
    }
    r = requests.get(api_url, params=params, headers=toutiao_headers)
    print(r.json())


def main():
    get_news_hot()


if __name__ == '__main__':
    main()
