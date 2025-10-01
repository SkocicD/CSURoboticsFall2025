import time
import socket

# FILL IN... what is the host for your own computer?
host =
# FILL IN... YOU PICK THIS PORT between 50000 and 65535
port =

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))     # Bind to address and port
s.listen()               # Listen for incoming connections

print(f"Server listening on {s}:{port}...")

conn, addr = s.accept()  # Accept a connection
print(f"Connected by {addr}")
while True:
    data = conn.recv(1024)  # Receive data (max 1024 bytes at a time)
    if not data:
        break
    print(f"Received: {data.decode('utf-8')}")
    time.sleep(.5)
