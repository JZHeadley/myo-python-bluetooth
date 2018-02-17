
import time
import socket

def main(HOST, PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    while True:
        sock.sendall("[!!!] RSSI Data will go here")
        time.sleep(0.1)

    sock.close()


if __name__ == '__main__':
    main('locahost', 8000)