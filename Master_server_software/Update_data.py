# code:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
from Server import MySelfServer
import socketserver
import socket


class Update_data(QThread):
    """更新数据类"""
    sinOut = pyqtSignal(list)

    def __init__(self, parent=None):
        super(Update_data, self).__init__(parent)
        HOST, PORT = "", 9999

        self.server = socketserver.ThreadingTCPServer((HOST, PORT), MySelfServer)
        # 实例化四个类其中之一并传入服务器地址和上面自己创建的服务器类，这里自己实例化的TCPServer

    def run(self):
        test_start_time = datetime.now()
        # 处理多个请求，这里注意的是虽然是处理多个请求，但是这句话并没有实现并发
        self.server.serve_forever()

    def server_stop(self):
        # self.server.server_close()
        client = socket.socket()
        client.connect(("127.0.0.1", 9999))
        msg = "shutdown"
        client.send(msg.encode())
        client.close()
