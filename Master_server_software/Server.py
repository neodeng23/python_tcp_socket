# 创建服务器用到的模块
import socketserver


class MySelfServer(socketserver.BaseRequestHandler):  # 第一步创建一个自己的server类，继承BaseRequestHandler类

    # 重写BaseRequestHandler类中的handle方法，直接写在自己创建的类中就可以了
    def handle(self):  # 里面的内容为服务器端跟客户端的所有交互
        stop_msg = "shutdown"
        while True:
            try:
                # 接收数据
                self.data = self.request.recv(1024).strip()
                rev_data = self.data.decode()

                # 打印客户端ip地址和发送来的数据，这里可能会问为什么会有self.client_address这个参数，这个在父类构造函数中
                print("{} wrote:".format(self.client_address[0]))
                print(rev_data)

                # 判断客户端是否断开
                if not self.data:
                    print(self.client_address, '的链接断开了！')  # 等待接收但接收为空则客户端断开
                    break

                if rev_data == stop_msg:
                    server.server_close()
                    self.request.close()
                    break
                else:
                    self.request.sendall(self.data.upper())  # 将接收到的数据大写发送回去

            except Exception as e:
                self.server.shutdown()
                self.request.close()
                break


if __name__ == "__main__":
    HOST, PORT = "", 9999

    # 第二步实例化四个类其中之一并传入服务器地址和上面自己创建的服务器类，这里自己实例化的TCPServer
    server = socketserver.ThreadingTCPServer((HOST, PORT), MySelfServer)

    # 处理多个请求，这里注意的是虽然是处理多个请求，但是这句话并没有实现并发
    server.serve_forever()
