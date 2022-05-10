try:
    import socket                            # Import socket module
except:
    print("You may need to install the socket module")

host = socket.gethostname()              # Get local machine name
port = 8000                        # Reserve a port for your service.
conn = socket.socket()                   # Create a socket object

conn.connect((host, port))

conn.sendall(b'Connected. Wait for data...') 

nickname = input("Nickname: ")
conn.sendall(nickname.encode('utf-8'))

while 1:
    intosend = input("message to send:")
    conn.sendall(intosend.encode('utf-8'))
    #data received back from sever
    data = conn.recv(1024)
    print("Data: ", data.decode('utf-8'))
conn.close()                                   # Close the socket when done


print(data.decode("utf-8"))
