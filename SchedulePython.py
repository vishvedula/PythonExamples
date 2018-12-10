#Usage of Python Timer to schedule a task

#!/usr/bin/python
from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day, hour=11, minute=35, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def hello_world():
        print ("hello world")
    #...

t = Timer(secs, hello_world)
t.start()
