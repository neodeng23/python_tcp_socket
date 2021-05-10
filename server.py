#!/usr/bin/env python
# 服务器端
import socket

host = "localhost"
port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
while 1:
    sock, addr = s.accept()
    print("got connection form " + sock.getpeername())
    data = sock.recv(1024)
    if not data:
        break
    else:
        print(data)
