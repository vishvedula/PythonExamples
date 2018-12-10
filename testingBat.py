#!/usr/bin/python
import os
from apscheduler.scheduler import Scheduler

# Start the scheduler
sched = Scheduler()
sched.start()

def job_function():
    os.system('D:\SimpleBatchFile.bat')

# Schedules job_function to be run on the third Friday
# of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
#sched.add_cron_job(job_function, month='6-8,11-12', day='3rd fri', hour='0-3')
sched.add_cron_job(job_function, day_of_week='mon-fri', hour=14, minute=48)
