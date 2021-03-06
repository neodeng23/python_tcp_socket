import socket

flag = True

# 生成socket对象
client = socket.socket()

# 链接要链接的ip和port（端口）
host = "192.168.172.232"
client.connect((host, 9999))

# while循环
while flag:

    # 获得用户输入
    msg = input("Enter your message('q' for quit):").strip()

    # 判断是否为空
    if len(msg) == 0:
        print("Message can't be empty")
        continue

    # 发送数据
    client.send(msg.encode())

    # 判断是否为'q'
    if msg != 'q':

        # 接收数据
        data = client.recv(1024)

        # 打印接收到的数据
        print(data)

    else:
        # 条件为False
        flag = False

# 关闭socket链接
client.close()
print('Connection is broken')