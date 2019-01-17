'''
import socket

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

#get address info like in client.py
addr_info = socket.getaddrinfo("www.google.com", 80, proto=socket.SOL_TCP)
(family, socketype, proto, canonname, sockaddr) = addr_info[0]



def main():
    #create socket 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #allows to reuse same bind port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)      

        s.bind((HOST, PORT))
        s.listen(1) #make socket listen
       
        #listen forever for connections
        while True:
            conn, addr = s.accept() #accept incoming connections
            print(conn)
            with conn:
                #create a socket
                with socket.socket(family, socketype) as proxy_end:
                    #connect 
                    proxy_end.connect(sockaddr)
                    
                    #grabbing the data from connected client
                    full_data = b""
                    while True:
                        data = conn.recv(BUFFER_SIZE)
                        if not data:
                           break
                        full_data += data
                    #sending to google
                    print(full_data)
                    proxy_end.sendall(full_data)
                    proxy_end.shutdown(socket.SHUT_WR)
                    #grab data from google
                    full_data_from_google = b""
                    while True:
                        data = proxy_end.recv(BUFFER_SIZE)
                        print("=====")
                        print(data)
                        if not data:
                            break
                        full_data_from_google += data
                        print(data)
                    conn.sendall(full_data_from_google)
            #print(full_data)
            #send data back as response
            #conn.sendall(full_data)
 

if __name__ == "__main__":
    main()  '''


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
                print("Received data: ",data)
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
