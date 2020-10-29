from socket import *
from datetime import datetime
import time
import threading
import os
import json

# HOST='192.168.72.1'
# HOST='10.40.37.46'
PORT=8888
BUFSIZ=1024

# 获取数据文件夹中的所有文件名
def get_dir_items(dir):
    return os.listdir(dir)


# 将要传输的文件以字节的方式取出放到变量content变量中
def get_data(items, number, file_path):
    with open(os.path.join(file_path,items[number]), "rb") as f:
        content = f.read()
    return content


# 将所有的ip地址放在hosts.txt中，广播时依次取出
def get_hosts():
    with open("hosts.txt","r") as f:
        hosts=f.readlines()
    return hosts





def send_data(HOST,content,number):
    ADDR = (HOST, PORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    tcpCliSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    content_length = len(content)
    print("发送数据给主机："+HOST+"  的第"+str(number+1)+"数据包的长度为：", content_length)
    # print("  数据长度为：", content_length)

    tcpCliSock.send(str(content_length).encode("utf-8"))
    time.sleep(0.1)
    tcpCliSock.send(content)
    while True:
        data = tcpCliSock.recv(BUFSIZ)

        if data:
            print(data.decode('utf-8'))
            break

    tcpCliSock.close()

def running_time(start,end,totaltime):
    starttime = start.strftime('%Y/%m/%d %H:%M:%S')
    terminaltime = end.strftime('%Y/%m/%d %H:%M:%S')

    filename = start.strftime('%Y-%m-%d-%H-%M-%S') + ".json"
    d = dict(starting_time=starttime,terminal_time=terminaltime, total_time=totaltime)

    # 存放运行时间信息的文件夹
    dir = "time"
    if not os.path.exists(dir):
        os.mkdir(dir)
    path = os.path.join(dir, filename)
    with open(path, "w") as f:
        json.dump(d, f, indent=6, separators=(',', ': '))

def main():
    start = datetime.now()

    threads=[]
    # 获得主机号，同时逐个给主机创建一个线程，发送代码文件
    hosts = get_hosts()
    file_path="data"
    items=get_dir_items(file_path)
    print("需要传输的文件个数为：",len(items))
    flag=True
    number=0
    while True:
        # for item in items:
        if len(items) == number:
            break
        if len(threads)!=0:
            for thread in threads:
                if thread.is_alive():
                    flag=False
                    break
        if flag:
            # 清空threads
            threads.clear()

            content = get_data(items,number,file_path)
            for host in hosts:
                # print("host:",host)
                t=threading.Thread(target=send_data,args=(host.strip(),content,number))
                threads.append(t)
                # print("当前子线程的个数为:",len(threads))

            for thread in threads:
                thread.start()

            # print("当前子线程状态", threads[0].is_alive())

            for thread in threads:
                thread.join()

            flag=True
            number+=1




    end=datetime.now()
    totaltime=(end-start).total_seconds()
    print("总时间为:",totaltime)

    running_time(start,end,totaltime)



main()