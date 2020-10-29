import psutil
import datetime
import time
import json

cpuinfo=psutil.cpu_times()
rate={}
cpu={}
for i in range(10):
    now=datetime.datetime.now()
    strnow=now.strftime('%Y/%m/%d %H:%M:%S')
    cpu[strnow]=cpuinfo

    print(strnow)
    print(cpuinfo.idle)
    print(cpuinfo.user)
    print(cpuinfo.system)
    print()

    rate[strnow] = 1-cpuinfo.idle/(cpuinfo.user+cpuinfo.system+cpuinfo.idle)
    time.sleep(1)

with open("cpu.json","w") as f:
    json.dump(cpu, f, indent=4)
with open("rate.json","w") as f:
    json.dump(rate, f, indent=4)

