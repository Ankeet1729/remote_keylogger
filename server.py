import socket

# Create Socket
host = '10.204.8.6'
port = 443
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen()

# Accept Client Connection
print("Waiting for client...")
conn,addr = s.accept()	        # Accept connection when client connects
print("Connected by " + addr[0])

# Print Client Data
while True:
	data = conn.recv(1024)	    # Receive client data
	if  data:
         print(data.decode('utf-8'))