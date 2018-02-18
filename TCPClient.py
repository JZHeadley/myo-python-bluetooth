
import socket


class TCPNode(object):

    def __init__(self, node_id, alarm_callback):
        self.alarm_callback = alarm_callback
        self.rssi = 0
        self.id = node_id
        self.sock = None
        self.host = None
        self.port = None

    def connect(self, host, port):
        self.host = host
        self.port = port
        # self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.settimeout(1)
        # self.sock.connect((self.host, self.port))
        failure = 1

        while failure != 0:
            print("failure", failure, failure != 0)
            try:
                self.sock.close()
            except:
                pass

            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(5)
            failure = int(self.sock.connect_ex((self.host, self.port)))
            print("[*] Attempting to connect. Error:", failure)
            time.sleep(2)

    def send(self, status, rssi):
        try:
            self.sock.send("{} {} {}".format(self.id, status, rssi).encode())
            self.recv(1024)
        except socket.error:
            self.sock.close()
            self.connect(self.host, self.port)

    def recv(self, rate):
        data = self.sock.recv(rate).decode()

        if data == "1":
            self.alarm_callback()



    def close(self):
        self.sock.close()


