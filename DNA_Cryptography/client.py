import socket
import random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from dna_encrypt import dna_encrypt_with_key

def generate_dynamic_key(length):
    bases = ['A', 'T', 'C', 'G']
    return ''.join(random.choices(bases, k=length))

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Receive the server's public key
    public_key_data = client_socket.recv(1024)
    public_key = RSA.import_key(public_key_data)
    print("Received public key from server.")

    # Generate a symmetric key
    symmetric_key = generate_dynamic_key(4)
    print(f"Generated symmetric key: {symmetric_key}")

    # Encrypt the symmetric key with the server's public key
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_key = cipher_rsa.encrypt(symmetric_key.encode())
    client_socket.send(encrypted_key)
    print("Sent encrypted symmetric key to server.")

    # Encrypt a message with the symmetric key
    plaintext = input("Enter plaintext to encrypt: ")
    encrypted_message = dna_encrypt_with_key(plaintext, symmetric_key)
    print(f"Encrypted message: {encrypted_message}")

    # Send the encrypted message to the server
    client_socket.send(encrypted_message.encode())

    client_socket.close()

if __name__ == "__main__":
    main()
