import psutil
import datetime
import json
import os



cpu_list=[]

start=datetime.datetime.now()
filename = start.strftime('%Y-%m-%d-%H-%M-%S') + ".json"

# 存放cpu信息的文件夹
dir = "cpu"
if not os.path.exists(dir):
    os.mkdir(dir)
filepath = os.path.join(dir, filename)

try:
    while True:

        now=datetime.datetime.now()
        currenttime = now.strftime('%Y/%m/%d %H:%M:%S')
        cpupercent=psutil.cpu_percent(interval=1)
        d=dict(current_time=currenttime,cpu_percent=cpupercent)
        cpu_list.append(d)

except KeyboardInterrupt:
    with open(filepath,"a+") as f:
        json.dump(cpu_list, f, indent=6,separators=(',', ': '))
        end=datetime.datetime.now()
        print("运行时间为:",(end-start).total_seconds())
# print(cpu_list)