import socket


payload = """GET / HTTP/1.1
Host: www.google.com\n
"""

def main():
    HOST = 'localhost'
    PORT = 8001
    address = (HOST, PORT)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=socket.SOL_TCP)
    client_socket.connect(address)
    print("Connected to the server.")

    client_socket.send(payload.encode())
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

if __name__ == "__main__":
    main()