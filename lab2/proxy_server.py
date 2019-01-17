# echo "Foobar" | nc localhost 8001
import socket

def main():
    HOST = "127.0.0.1"
    PORT = 8001
    address = (HOST, PORT)

    GOOG_HOST = "www.google.com"
    GOOG_PORT = 80
    addr_info = socket.getaddrinfo(GOOG_HOST, GOOG_PORT, proto=socket.SOL_TCP)
    proxy_addr = addr_info[0]

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(address)
    server.listen(5)

    try:
        while(True):
            print("start listenning...")
            client, _ = server.accept()

            # getting data from client
            response = b""
            while(True):
                data = client.recv(1024)
                if not data:
                    break
                print("Received requests: ",data)
                response += data

            # transferring recevied data to google
            data_from_goole = b""
            (family, sockettype, proto, _, sockaddr) = proxy_addr
            with socket.socket(family, sockettype, proto=proto) as proxy_end:
                proxy_end.connect(sockaddr)
                proxy_end.sendall(response)
                proxy_end.shutdown(socket.SHUT_WR)

                # getting google's response
                while (True):
                    data = proxy_end.recv(1024)
                    if not data:
                        break
                    data_from_goole += data

            client.sendall(data_from_goole)
            client.close() 
    except Exception as e:
        print(e)
        server.close()
        pass
    server.close()
    

main()
