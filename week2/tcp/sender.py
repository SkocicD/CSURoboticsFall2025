import socket

# FILL IN... what is the host for your own computer?
host = 'localhost'
# YOU PICK THIS PORT between 50000 and 65535
port = 50001


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))  # Connect to the server
print(f"Connected to {host}:{port}")

# fill in the message you want to send
message = 'david'

s.sendall(message.encode('utf-8'))  # Send a message
print(f"Sent: {message}")
