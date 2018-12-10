#!/usr/bin/python
from datetime import datetime, timedelta

while 1:
    print 'Run something..'

    dt = datetime.now() + timedelta(hours=1)
    dt = dt.replace(minute=10)

    while datetime.now() < dt:
        time.sleep(1)
