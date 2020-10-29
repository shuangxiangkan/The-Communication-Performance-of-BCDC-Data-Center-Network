from socket import *
from time import ctime

# 标准写法，具体含义见网上
HOST='10.40.33.49'
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
# 下面这句代码就是为了解决之前出现到“Address already in use” 这个问题
# 好像是因为绑定到IP在程序结束之后还要被占用几分钟，这句代码就是为了让系统运行完立马释放IP
# 还想继续了解的话，去百度搜一下，可以写关键字，linux python socket Address already in use
tcpSerSock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

while True:
    print('waiting for connection...')
    # 接收到socket和发送到主机地址
    tcpCliSock,addr=tcpSerSock.accept()

    # 接受数据
    length=tcpCliSock.recv(BUFSIZE)
    # 因为发送到都是字节流，要想看懂，数据需要解码
    print("主机："+str(addr)+"  发送的数据长度为："+length.decode("utf-8"))
    data_length=0
    while True:
        data=tcpCliSock.recv(BUFSIZE)
        # 没有数据，跳出循环
        if not data:
            break

        # 不断累加数据长度
        data_length+=len(data)
        # 判读接收到的数据长度是否和需要接收到的数据长度相同，相同则跳出循环
        if data_length==int(length.decode('utf-8')):
            print("本机接收到的数据长度：",data_length)
            break
    response="主机："+HOST+"  接收到的数据长度为："+str(data_length)
    # 数据加码传送
    tcpCliSock.send(response.encode("utf-8"))

    tcpCliSock.close()
tcpCliSock.close()