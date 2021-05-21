import socket
import time
from logger import Logger


def SendAndRev(msg, host, port):
    now_time = time.strftime('%Y%m%d')
    log_name = now_time + ".log"
    log = Logger(log_name, level='debug')
    client = socket.socket()
    log.logger.info('begin try to connect to host: ' + host + ":" + str(port))
    try:
        client.connect((host, port))
        log.logger.info('Success to connect to host: ' + host + ":" + str(port))
        client.send(msg.encode())
        data = client.recv(1024)
        log.logger.info('get infomation from  host: ' + host + ":" + str(port) + ":" + data.decode())
        client.close()
        return data.decode()
    except:
        log.logger.warning('Fail to connect to host: ' + host + ":" + str(port))
        return "no connect"


msg = "aaaa"
data = SendAndRev(msg, "127.0.0.1", 9999)
print(data)
