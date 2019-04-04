import time

from db.model import IPInfo, OrderID
from proxy_pool.mp import get_mp_ip, get_order_id
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from config import mp_url
import json

"""
定时任务调度
"""


def job_get_order_id():
    """
    定时获得并保存订单id
    :return:
    """
    order_id = get_order_id()
    OrderID.insert(order_id=order_id, time=int(time.time())).on_conflict_ignore().execute()
    print("定时获取订单号")


def job_get_proxy():
    """
    定时获取代理ip，并保存到数据库
    :return:
    """
    # 订单号初始化

    # 检查订单id 有效性
    order_id = OrderID.select().order_by(OrderID.time.desc())
    if not order_id.exists():
        job_get_order_id()
        return
    now_time = int(time.time())  # 当前 Unix时间戳（秒）
    interval = 5000  # 每5000秒重新注册账号
    if order_id[0].time + interval < now_time:
        job_get_order_id()
        return
    data = get_mp_ip(url=mp_url.format(order_id[0].order_id), types='text')
    # 处理数据格式
    if data:
        try:
            data = data.replace("ip:port", "ip_port")
            data = json.loads(data)
            print(data)
            #  插入重复IP数据时 更新数据
            IPInfo.insert_many(data['result']).on_conflict_replace().execute()
        finally:
            print('定时获取IP')


# 实例化调度器
scheduler_get_proxy = BlockingScheduler()
scheduler_get_id = BackgroundScheduler()

# 定时运行
# 'cron', seconds='*/15'  hours=5,
scheduler_get_proxy.add_job(job_get_proxy, 'interval', seconds=20)
scheduler_get_id.add_job(job_get_order_id, 'interval', seconds=1, hours=2)

# 开始运行调度器
scheduler_get_id.start()
scheduler_get_proxy.start()
