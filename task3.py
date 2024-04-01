#Server
import socket 
s = socket. socket(socket.AF_INET, socket.SOCK_STREAM) 
port = 5004 
s. bind((socket.gethostname(), port)) 
s. listen(100) 
while True: 
        c, adr =s. accept() 
        print(f"Connected to {adr} established") 
        c.send(bytes("He110 from server", "utf-8")) 
        data =c. recv(1024) 
        print("received from client: ", data.decode()) 
        c. close()

#CLient
import socket 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
port = 5004 
client.connect((socket.gethostname(), port)) 
print(f"Connected to server at {socket.gethostname()}:{port}") 
 
message_to_server = "Hello from the client!" 
client.send(bytes(message_to_server, 'utf-8')) 
 
data = client.recv(1024) 
print("Received from server:", data.decode()) 
 
client.close()