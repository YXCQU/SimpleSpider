import requests
import config
import json
from spider.HtmlDownloader import download


class Weibopider(object):
    def get_comments(self, weiboid='4160547165300149', page=1, ip_port=None):
        """
        获得某条微博的评论
        :param weiboid: 某条微博id
        :param page: 评论页数, 默认是 1
        :param ip_port: 代理ip, 格式(IP:port), 如 127.0.0.1:8080
        :return: 第page页的评论
        """
        url = "https://m.weibo.cn/api/comments/show/"
        params = {
            'id': weiboid,
            'page': page
        }

        try:
            # r = requests.get(url, headers=self.headers, params=params)
            r = download(url, headers=config.weibo_headers, params=params, ip_port=ip_port)
            comment_json = json.loads(r)
            if comment_json['msg'] == '数据获取成功':
                return comment_json
            else:
                return None
        except Exception as e:
            print(e)
            return None

    def get_hot_comments(self, weiboid='4160547165300149', page=1, ip_port=None):
        url = "https://m.weibo.cn/single/rcList"
        params = {
            'format': 'cards',
            'id': weiboid,
            'type': 'comment',
            'hot': 1,
            'page': page,
        }
        try:
            # r = requests.get(url, headers=self.headers, params=params)
            r = download(url, headers=config.weibo_headers, params=params, ip_port=ip_port)
            comment_json = json.loads(r)
            return comment_json
        except Exception as e:
            print(e)
            return None


if __name__ == '__main__':
    wb = Weibopider()
    print(wb.get_hot_comments())
