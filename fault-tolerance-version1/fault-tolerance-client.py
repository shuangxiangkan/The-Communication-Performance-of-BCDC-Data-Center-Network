from socket import *
from datetime import datetime
import threading
import time
import json
import os
import psutil

# 标准写法，具体参见网上关于socket方面的解释
# HOST='192.168.72.1'
PORT=8888
BUFSIZ=1024


threads=[]

# 获取数据文件夹中的所有文件名
def get_dir_items(dir):
    return os.listdir(dir)


# 将要传输的文件以字节的方式取出放到变量content变量中
def get_data(file):
    # 以二进制形式打开文件
    with open(file,"rb") as f:
        # 将文件file中的数据存到content中
        content=f.read()
    return content




def send_data(HOST):
    # 绑定IP和端口
    ADDR = (HOST, PORT)
    # 这句是socket的标准写法，具体参数的意义上网查一下就可以了
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    # 下面这句代码就是为了解决当时出现的"Address already in use"这个问题
    # 好像是因为绑定的ip在程序结束之后还要被占用几分钟，这句代码就是为了让系统在程序运行完立马释放ip
    # 还想继续了解的话，去百度搜一下,可以写关键字linux python socket Address already in use来搜索
    tcpCliSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    # 初试时所有数据文件的长度为0
    content_length=0
    # 这是和这个.py文件在同一目录下的data文件夹，data文件夹中存放的是需要传输的数据文件
    dir='data'
    # 获得所有的数据文件名，所有的文件名都存在字典files中
    files=get_dir_items(dir)
    # 计算所有数据文件的大小
    for file in files:
        # os.path.join(dir,file)这个函数是将文件夹名和文件名连接起来，形成一个相对路径名，如,dir=data,file=data1.zip,
        # 然后这函数得到的值为data\data1.zip
        # os.path.getsize(file)函数的作用是得到file这个文件的大小
        content_length+=os.path.getsize(os.path.join(dir,file))
    # 将所有数据的总长度发送给服务器
    # 需要先变成字节流再传送
    tcpCliSock.send(str(content_length).encode("utf-8"))
    print("发送数据给主机：" + HOST + "  数据长度为：", content_length)
    # 逐个读取并发送数据
    for file in files:
        # print(os.path.join(dir,file))
        # 得到每个文件的数据流
        content=get_data(os.path.join(dir,file))
        # 发送数据给服务器
        tcpCliSock.send(content)
        # 等待0.1s后发送下一个数据包
        time.sleep(0.5)

    while True:
        # 接收到的数据
        data = tcpCliSock.recv(BUFSIZ)

        # 如果数据不为空，则将数据打印出来，然后跳出循环
        if data:
            # 传送的是字节流，要想被看懂，需要先解码
            print(data.decode('utf-8'))
            break
    # 关闭socket
    tcpCliSock.close()

def cpu_data():
    list=[]
    while threads[0].isAlive():
        starttime = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        d = dict(current_time=starttime, cpu_percent=psutil.cpu_percent(interval=1))
        list.append(d)
    filename = datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".json"

    # 存放cpu信息的文件夹
    dir = "cpu"
    if not os.path.exists(dir):
        os.mkdir(dir)
    path = os.path.join(dir, filename)
    with open(path, "w") as f:
        json.dump(list, f, indent=6,separators=(',', ': '))


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


    # 程序开始运行的时间
    start = datetime.now()

    # host = "10.10.66.6"
    # host="10.40.33.228"
    host="39.107.124.107"
    # send_data(host)

    t1 = threading.Thread(target=send_data, args=(host,))
    t2=threading.Thread(target=cpu_data)
    threads.append(t1)
    threads.append(t2)


    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


    # 程序结束时的当前时间
    end=datetime.now()
    totaltime = (end - start).total_seconds()
    print("总时间为:",totaltime)

    running_time(start,end,totaltime)


if __name__ == '__main__':
    main()