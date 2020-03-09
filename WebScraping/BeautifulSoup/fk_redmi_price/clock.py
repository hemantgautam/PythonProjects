from apscheduler.schedulers.blocking import BlockingScheduler
from flipkart import check_myntra_product_price
sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=5)
def scheduled_job():
	check_myntra_product_price()
    print('This job is run every weekday at 5pm UTC which is 10:30am IST')

sched.start()