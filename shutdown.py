import os
import datetime

shutdown = '22:25'

while True:
    now = datetime.datetime.now()
    time = now.strftime('%H:%M')
    if time == shutdown:
        os.system("shutdown /s /t 1")
        break