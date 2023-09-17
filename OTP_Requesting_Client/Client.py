import socket
salt = 5000908999
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1', 55465))
data = client_socket.recv(1024).decode('ascii')

print("This is the received OTP")
print(int(data)-salt)
