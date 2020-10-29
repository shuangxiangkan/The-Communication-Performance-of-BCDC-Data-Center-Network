import psutil


while True:
    print(psutil.cpu_percent(interval=1))
    # print(psutil.cpu_percent(interval=1,percpu=False))
    # print(psutil.cpu_percent(interval=1, percpu=True))

