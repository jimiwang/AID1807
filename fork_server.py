from socket import *
import os,sys
import signal

#客户端处理函数
def client_handler(c):
    print("处理子进程的请求:",c.getpeername())
    try:
        while 1:
            data = c.recv(1024)
            if not data:
                break
            print(data.decode())
            c.send('收到客户端强求'.encode())
    except (KeyboardInterrupt,SystemError):
        sys.exit("客户端退出")
    except Exception as e:
        print(e)
    c.close()
    sys.exit(0)

#创建套接字
HOST = ''
PORT = 8888
ADDR = (HOST,PORT)
s = socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)
print("进程%d等待客户端链接"%os.getpid())
#在父进程中忽略子进程状态改改变，子进程退出自动由操作系统处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

while 1:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print("Error",e)
        continue

    #为客户端创建新的进程,处理请求
    pid = os.fork()
    if pid == 0:
        s.close()
        client_handler(c)


    #父进程或者创建失败都继续等待下个客户链接
    else:
        c.close()
        continue








