
import time
import threading
import socket

def client_handler(client):
    while True:
        data = client.recv(4096)

        if len(data) == 0:
            break

        print("[+] data:", data)

def main(HOST, PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))

    sock.listen(10)

    while True:
        client, addr = sock.accept()
        print("[+] Connection with", addr)

        t = threading.Thread(target=client_handler, args=(client,))
        t.start()

if __name__ == '__main__':
    main('localhost', 8080)