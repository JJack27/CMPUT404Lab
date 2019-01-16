# Author: Yizhou Zhao

import socket

def main():
    HOST = socket.gethostbyname('www.google.com')
    PORT = 80
    address = (HOST, PORT)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(address)
    print("Connected to the server.")

    request = "GET / HTTP/1.1\n\n"
    client_socket.send(request.encode())
    while True:
        data = client_socket.recv(1024)
        print(data)
        if "</body></html>\r\n0\r\n\r\n".encode() in data or not data:
            print("Disconnect")
            client_socket.close()
            break
        



main()