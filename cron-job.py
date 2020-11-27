from crontab import CronTab
import os
basedir = os.path.dirname(os.path.realpath(__file__))
USER = "root"
cron = CronTab(user=USER)
job = cron.new(command = f"python3 {os.path.join(basedir,'export_db.py')}")
job.minute.every(1)
cron.write()
