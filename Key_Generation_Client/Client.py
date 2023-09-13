import socket
import rsa
from Secret_Phrase_Generator import generate_int_from_random
from RSA_encrypt_decrypt import encrypt

server_ip = '127.0.0.1'
server_port = 55540
client_id = '1'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip, server_port))

public_key_bytes_received = sock.recv(4096)

received_public_key = rsa.PublicKey.load_pkcs1(public_key_bytes_received)

print("Received Public Key: " + str(received_public_key))

with open("public_Key_Server.pem", 'wb') as p:
    p.write(received_public_key.save_pkcs1('PEM'))

while True:
    try:
        user_input = int(input("Please enter an integer Value: "))
        break

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print("You entered:", user_input)

send = user_input

# This is the generated X
secret_phrase = str(generate_int_from_random(send, int(client_id)))
print(f'The secret phrase is: {secret_phrase}')

# This is th encrypted X
encrypted_data = encrypt(secret_phrase, received_public_key)

print("This is the encrypted format of the secret phrase")
print(encrypted_data)

sock.send(encrypted_data)
sock.send(client_id.encode('utf-8'))

sock.close()
