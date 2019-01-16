- Question 1: How do you specify a TCP socket in Python?
    - When we are using `AF_INET` family and `SOCK_STREAM` type, we know that the socket must be a TCP sockket.
- Question 2: 
    - The server are running all the time and waiting for incomming connections and requests. And it will responds to client's requests. And it has to bind with a host and a port.
    - The client side can only run properly when the server side is running. Client side initiate the connection by sending HTTP requests to the server. 
    - Usually, server cannot sent message to clients unless clients have sent a request, due to the firewall.
- Question 3
    - we set `SO_REUSEADDR` to `True` to do it. Here is how it's done 
    ```python
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ```
- Question 4
    - 
