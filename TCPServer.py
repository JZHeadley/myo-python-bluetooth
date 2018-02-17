
import threading
import socket

def client_handler(client):
    while True:
        data = client.recv(1024)

        if not data:
            break

        print "[+] data: %s" % data 

def main(HOST, PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))

    sock.listen(4)

    while True:
        client, addr = sock.accept()
        print "[+] Connection with %s" % addr

        t = threading.Thread(target=client_handler, args=(client,))
        t.start()

    sock.close()

if __name__ == '__main__':
    main('localhost', 8000)