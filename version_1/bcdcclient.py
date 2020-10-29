from socket import *
from datetime import datetime
import time
import threading

# HOST='192.168.72.1'
# HOST='10.40.37.46'
PORT=21567
BUFSIZ=1024

# 将要传输的文件以字节的方式取出放到变量content变量中
with open("data2.zip","rb") as f:
    content=f.read()


# 将所有的ip地址放在hosts.txt中，广播时依次取出
def get_hosts():
    with open("hosts.txt","r") as f:
        hosts=f.readlines()
    return hosts





def send_data(HOST):
    ADDR = (HOST, PORT)
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    tcpCliSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    content_length = len(content)
    print("发送数据给主机："+HOST+"  数据长度为：", content_length)
    # print("  数据长度为：", content_length)

    tcpCliSock.send(str(content_length).encode("utf-8"))
    time.sleep(0.1)
    tcpCliSock.send(content)
    while True:
        data = tcpCliSock.recv(BUFSIZ)

        if data:
            print( data.decode('utf-8'))
            break

    tcpCliSock.close()

def main():
    start = datetime.now()

    threads=[]
    # 获得主机号，同时逐个给主机创建一个线程，发送代码文件
    hosts = get_hosts()
    for host in hosts:
        # print("host:",host)
        t=threading.Thread(target=send_data,args=(host.strip(),))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()




    end=datetime.now()
    print("总时间为:",(end-start).total_seconds())




main()