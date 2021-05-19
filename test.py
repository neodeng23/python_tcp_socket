# code:utf-8
from PyQt5.QtCore import *
from Master_server_ui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QFont
from PyQt5.QtCore import Qt
import socketserver
import socket
import time
import sys

pe_red = QPalette()
pe_red.setColor(QPalette.WindowText, Qt.red)

pe_green = QPalette()
pe_green.setColor(QPalette.WindowText, Qt.green)

pe_yel = QPalette()
pe_yel.setColor(QPalette.WindowText, Qt.yellow)


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.thread = Update_data()
        self.thread.sinOut.connect(self.log_Add)
        self.thread.start()

    def closeEvent(self, event):
        result = QMessageBox.question(self, "注意：", "您真的要关闭窗体吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            self.thread.server_stop()
            self.thread.quit()
            event.accept()
        else:
            event.ignore()

    def log_Add(self, item):
        self.log_table.update_item_data(item)


class Update_data(QThread):
    """更新数据类"""
    sinOut = pyqtSignal(list)

    def __init__(self, parent=None):
        super(Update_data, self).__init__(parent)
        HOST, PORT = "", 9999

        self.server = socketserver.ThreadingTCPServer((HOST, PORT), MySelfServer)
        # 实例化四个类其中之一并传入服务器地址和上面自己创建的服务器类，这里自己实例化的TCPServer

    def run(self):
        # 处理多个请求，这里注意的是虽然是处理多个请求，但是这句话并没有实现并发
        self.server.serve_forever()

    def server_stop(self):
        # self.server.server_close()
        client = socket.socket()
        client.connect(("127.0.0.1", 9999))
        msg = "shutdown"
        client.send(msg.encode())
        client.close()


# 创建服务器用到的模块
class MySelfServer(socketserver.BaseRequestHandler):  # 第一步创建一个自己的server类，继承BaseRequestHandler类

    # 重写BaseRequestHandler类中的handle方法，直接写在自己创建的类中就可以了
    def handle(self):  # 里面的内容为服务器端跟客户端的所有交互
        stop_msg = "shutdown"
        while True:
            try:
                # 接收数据
                self.data = self.request.recv(1024).strip()
                rev_data = self.data.decode()
                now_time = time.strftime('%Y%m%d-%H%M%S')
                # 打印客户端ip地址和发送来的数据，这里可能会问为什么会有self.client_address这个参数，这个在父类构造函数中
                print("{} wrote:".format(self.client_address[0]))
                print(rev_data)
                if rev_data == "":
                    rev_data = "connection finish"
                log_data = [now_time, self.client_address[0], "connect", rev_data, "PLC1"]
                # ["Time", "DUT", "Process", "CMD", "PLC"]
                MyMainForm.log_Add(mainWindow, log_data)
                # 判断客户端是否断开
                if not self.data:
                    print(self.client_address, '的链接断开了！')  # 等待接收但接收为空则客户端断开
                    break

                if rev_data == stop_msg:
                    self.server.server_close()
                    self.request.close()
                    break
                else:
                    self.request.sendall(self.data.upper())  # 将接收到的数据大写发送回去

            except Exception as e:
                self.server.shutdown()
                self.request.close()
                break


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyMainForm()
    mainWindow.show()
    sys.exit(app.exec_())
