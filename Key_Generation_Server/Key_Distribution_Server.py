import socket
import random

all_keys = []
salt = 5000908999

with open("key_store.txt",'r') as file:
    for line in file:
        cleaned_line = line.strip()
        all_keys.append(cleaned_line)

def choose_key(key_list):
    size = len(key_list)
    index = random.randint(0, size-1)
    print(index)
    return int(key_list[index]) + salt


# print(all_keys)
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 55465))
server_socket.listen(5)

while True:
    print("Waiting for the connection form the OTP requesting client......")
    connection,client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    print("Send the key from the key store: ")
    OTP = choose_key(all_keys)

    connection.send(str(OTP).encode('ascii'))

