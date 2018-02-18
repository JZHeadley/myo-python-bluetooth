
import time
import socket


class TCPNode(object):

    def __init__(self, node_id, alarm_callback):
        self.alarm_callback = alarm_callback
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.rssi = 0
        self.id = node_id

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, status, rssi):
        self.sock.send("{} {} {}".format(self.id, status, rssi).encode())
        self.recv(1024)

    def recv(self, rate):
        data = self.sock.recv(rate).decode()

        if data == "1":
            self.alarm_callback()



    def close(self):
        self.sock.close()


