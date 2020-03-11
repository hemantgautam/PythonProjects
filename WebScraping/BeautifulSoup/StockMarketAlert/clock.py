from apscheduler.schedulers.blocking import BlockingScheduler
from stock import get_stock_alert

sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=3)
# @sched.scheduled_job('interval', day_of_week='mon-fri')
@sched.scheduled_job('cron', day_of_week='mon-sun', hour='4-11')
def scheduled_job():
    get_stock_alert()
    print('This job runs Monday to friday every 1 hour form')

sched.start()
