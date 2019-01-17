# Author: Yizhou Zhao

import socket

HOST = "www.google.com" #socket.gethostbyname('www.google.com')
PORT = 80
BUFSIZ = 1024
payload = """GET / HTTP/1.1
Host: {HOST}

""".format(HOST=HOST)


def connect_socket(addr):
    (family, sockettype, proto, _, sockaddr) = addr
    try:
        s = socket.socket(family, sockettype, proto)
        s.connect(sockaddr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)
        response = b""
        while True:
            data = s.recv(BUFSIZ)
            if not data:
                break
            response += data
        print(response)
    except Exception as e:
        print(e)
        pass
'''
def main():
    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)
    addr = addr_info[0]
    connect_socket(addr)

'''
def main():
    HOST = socket.gethostbyname('www.google.com')
    PORT = 80
    address = (HOST, PORT)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=socket.SOL_TCP)
    client_socket.connect(address)
    print("Connected to the server.")

    request = "GET / HTTP/1.1\n\n"
    client_socket.send(request.encode())
    client_socket.shutdown(socket.SHUT_WR)
    response = b""
    try:
        while True:
            data = client_socket.recv(1024)
            
            if not data:
                print("Disconnect")
                client_socket.close()
                break
            response += data
    except Exception as e:
        print(e)
        pass
    print(response)
        


main()