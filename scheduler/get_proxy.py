from db.model import IPInfo
from proxy.mimvp_proxy import get_mp_ip
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from config import mp_url
import json

# 实例化调度器
scheduler = BlockingScheduler()


def job():
    """
    获取代理ip，并保存到数据库
    :return:
    """
    data = get_mp_ip(url=mp_url, types='text')
    # 简单处理下数据格式
    if data:
        try:
            data = data.replace("ip:port", "ip_port")
            data = json.loads(data)
            IPInfo.insert_many(data['result']).on_conflict_ignore().execute()
        finally:
            print('定时获取IP')


# 定时运行 间隔15s
scheduler.add_job(job, 'interval', seconds=15)

# 开始运行调度器
scheduler.start()
