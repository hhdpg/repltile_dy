import socket
import sys
socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
socket_server.bind((host,port))
socket_server.listen(5)
while True :
    clientsocket,addr = socket_server.accept()
    print("连接地址：%s" % str(addr))
    msg = "'欢迎访问菜鸟'+'\r\n'"
    clientsocket.send(msg.encode("utf-8"))
    clientsocket.close()