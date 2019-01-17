# echo "Foobar" | nc localhost 8001
import socket

def main():
    HOST = "127.0.0.1"
    PORT = 8001
    address = (HOST, PORT)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(address)
    server.listen(5)

    try:
        while(True):
            client, _ = server.accept()
            response = ""
            while(True):
                data = client.recv(1024)
                if not data:
                    break
                message = data.decode().strip()
                print("Received data: ",message)
                response += message
            response += "\n"
            client.sendall(response.encode())
            client.close() 
    except Exception as e:
        print(e)
        server.close()
        pass
    server.close()
    

main()
