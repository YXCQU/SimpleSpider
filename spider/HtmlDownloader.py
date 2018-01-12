import config
import requests
import chardet


def download(url, headers=config.get_header(), ip_port=None, params=None):
    """
    封装了常用网络请求功能
    :param url: 请求的url
    :param headers: 请求的headers
    :param ip_port: 代理ip：port
    :param params: 请求参数
    :return:
    """
    try:
        r = requests.get(url=url, headers=headers, timeout=config.TIME_OUT, params=params)
        r.encoding = chardet.detect(r.content)['encoding']
        if (not r.ok) or len(r.content) < 1:
            raise ConnectionError
        else:
            return r.text

    except Exception as e:
        print(e)
        retry_count = 0  # 重试次数
        if ip_port:
            proxies = {"http": "http://%s:%s" % ip_port, "https": "http://%s:%s" % ip_port}
        else:
            proxies = None

        while retry_count < config.RETRY_TIME:
            try:
                r = requests.get(url=url, headers=headers, timeout=config.TIMEOUT, proxies=proxies)
                encode = chardet.detect(r.content)['encoding']
                if encode is 'json':
                    r.encoding = 'utf-8'
                if (not r.ok) or len(r.content) < 1:
                    raise ConnectionError
                else:
                    return r.text
            except Exception as e:
                print(e)
                retry_count += 1


