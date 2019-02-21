import time
from datetime import datetime as dt
from datetime import date, time, timedelta

hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

tn = dt.now().year,dt.now().month,dt.now().day,dt.now().hour,dt.now().minute,dt.now().second #TimeNow
mt = dt.now().year,dt.now().month,dt.now().day,8,dt.now().minute,dt.now().second #morningtime
et = dt.now().year,dt.now().month,dt.now().day,21,dt.now().minute,dt.now().second #eveningtime
nmt = mt + timedelta(days+=1) #NextMorningtime

while True:
    if mt < tn < et:
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")

#test lastline
with open(hosts_path,'r') as file:
    content=file.readlines()
    print(content[-1][-2][-3])

#set sleeptime to conserve resources on computer (if it unneccessarily runs all the time then it wastes computer resources)
if tn > et:
    sleeper = (nmt - tn).total_seconds() #if it's past evening time then sleep till next morning working time

elif tn < et and tn > mt: #if it's working time, then sleep till evening time
    sleeper = (et-tn).total_seconds()
else:
    sleeper = (mt-tn).total_seconds() #if it's early morning then sleep till morning working time

sleeptime = sleeper

time.sleep(sleeptime)
