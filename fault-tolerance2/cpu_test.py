import psutil
import datetime
import json
import os

cpu_list=[]

for i in range(10):

    now=datetime.datetime.now()
    currenttime = now.strftime('%Y/%m/%d %H:%M:%S')
    cpupercent=psutil.cpu_percent(interval=1)
    d=dict(current_time=currenttime,cpu_percent=cpupercent)
    cpu_list.append(d)

dir="cpu"
file= "cpu"+datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')+".json"
filepath=os.path.join(dir,file)
with open(filepath,"w") as f:
    json.dump(cpu_list, f, indent=6,separators=(',', ': '))
# print(cpu_list)