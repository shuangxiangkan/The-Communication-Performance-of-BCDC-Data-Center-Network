from socket import *
from time import ctime

HOST='10.40.32.195'
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
tcpSerSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

while True:
    print('waiting for connection...')
    tcpCliSock,addr=tcpSerSock.accept()
    # print('connection from:',addr)

    length=tcpCliSock.recv(BUFSIZE)
    print("主机："+str(addr)+"  发送的数据长度为："+length.decode("utf-8"))
    data_length=0
    while True:
        data=tcpCliSock.recv(BUFSIZE)
        if not data:
            break

        data_length+=len(data)

        if data_length==int(length.decode('utf-8')):
            print("本机接收到的数据长度：",data_length)
            break
    response="主机："+HOST+"  接收到的数据长度为："+str(data_length)
    tcpCliSock.send(response.encode("utf-8"))

    tcpCliSock.close()
tcpCliSock.close()