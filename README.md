# Decentralised_OTP_Generator
The Secure OTP Generation and Distribution System is a robust solution designed to enhance the
security of OTP (One-Time Password) generation and distribution. OTPs play a important role in secure
authentication, and this project aims to elevate their security levels through advanced cryptographic
techniques and decentralized architecture


#  Implementation Steps:

### 1. Public Key Exchange:
* Key Generation Clients initiate communication with the Key Generation Server.
* The clients request the public key from the server.
* The server sends its public key to the clients.

### 2. User Input and Secret Phrase Generation:
* Each Key Generation Client takes an integer input from the user.
* Using the provided integer, the client generates a secret phrase by combining it with a random
number and the client's unique identifier (client_id).
* The client determines which hash algorithm to use based on its client_id.
* The secret phrase is hashed using the selected algorithm.

### 3. RSA Encryption:
* The client encrypts the secret phrase using the server's public key.
* This ensures that the secret phrase is securely transmitted to the server.

### 4. Data Transmission to Server:
* The client sends the encrypted data (secret phrase) to the Key Generation Server.
* The client also sends its client_id for identification.

### 5. Decryption and Hashing on Server:
* The Key Generation Server receives the encrypted data and decrypts it using its private key.
* The server hashes the decrypted data multiple times.
* The resulting value is stored in the Key Distribution Server.

### 6. OTP Request by Client:
* When a Key Requesting Client needs an OTP, it sends a request to the Key Distribution Server.

### 7. OTP Distribution:
* The Key Distribution Server responds with the OTP data, including a salt value.
* The Key Requesting Client receives the OTP data.

### 8. Salt Removal and OTP Usage:
* The Key Requesting Client extracts the salt value from the received data.
* The OTP is calculated by removing the salt from the received data.
