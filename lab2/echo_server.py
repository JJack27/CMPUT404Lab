import socket

def main():
    HOST = "127.0.0.1"
    PORT = 8001
    address = (HOST, PORT)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(address)
    server.listen(5)

    while(True):
        client, _ = server.accept()
        print(client)
        response = "".encode()
        print("connected")
        while(True):
            data = client.recv(1024)
            if not data:
                break
            print("Received data: ",data.decode().strip())
            response += data  
        client.send(response)
        client.close() 
    server.close()
    

main()

