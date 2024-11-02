import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from dna_decrypt import dna_decrypt_with_key

# Generate RSA keys for secure key exchange
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()
    return private_key, public_key

def start_server():
    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening for connections...")

    private_key, public_key = generate_rsa_keys()
    print("RSA keys generated.")

    # Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    # Send the public key to the client
    conn.send(public_key.export_key())
    print("Sent public key to client.")

    # Receive the encrypted symmetric key from the client
    encrypted_key = conn.recv(256)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    symmetric_key = cipher_rsa.decrypt(encrypted_key).decode()
    print(f"Received and decrypted symmetric key: {symmetric_key}")

    # Receive the encrypted message from the client
    encrypted_message = conn.recv(1024).decode()
    print(f"Received encrypted message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = dna_decrypt_with_key(encrypted_message, symmetric_key)
    print(f"Decrypted message: {decrypted_message}")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
