from datetime import datetime
import os
import time
import datetime
import  pipes
import subprocess

basedir = os.path.dirname(os.path.realpath(__file__))
# Database details
DBCREDENTIAL = os.path.join(basedir,'mysqldump.cnf')
TABLE = 'users'
DBNAME = 'test'

###########################
BACKUPPATH = os.path.join(basedir,'backups')
DATETIME = time.strftime('%Y%m%d-%H%M%S')
FILENAME = os.path.join(BACKUPPATH,f"{TABLE}_{DATETIME}_dump.sql")

try:
    os.stat(BACKUPPATH)
except:
    os.mkdir(BACKUPPATH)

dumpCommand = f"mysqldump --defaults-extra-file={DBCREDENTIAL} {DBNAME} {TABLE} > {FILENAME}"
os.system(dumpCommand)
#subprocess.Popen(dumpCommand,shell=True)