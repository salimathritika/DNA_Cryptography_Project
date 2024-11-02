import socket
import threading
from tkinter import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from dna_decrypt import dna_decrypt_with_key

# Server class with GUI
class ServerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("DNA Cryptography Server")
        self.master.geometry("400x300")

        # Generate RSA keys
        self.private_key, self.public_key = self.generate_rsa_keys()

        # GUI Components
        Label(master, text="Public Key:").pack()
        self.pubkey_text = Text(master, height=5, width=40)
        self.pubkey_text.pack()
        self.pubkey_text.insert(END, self.public_key.export_key().decode())

        Button(master, text="Start Server", command=self.start_server).pack()
        self.msg_label = Label(master, text="Received Decrypted Message:")
        self.msg_label.pack()
        self.decrypted_msg_text = Text(master, height=5, width=40)
        self.decrypted_msg_text.pack()

    def generate_rsa_keys(self):
        key = RSA.generate(2048)
        return key, key.publickey()

    def start_server(self):
        # Clear the decrypted message box each time the server starts
        self.decrypted_msg_text.delete("1.0", END)

        # Create socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 12345))
        self.server_socket.listen(1)
        print("Server is listening for connections...")

        # Start a new thread to accept the client connection
        threading.Thread(target=self.accept_client).start()

    def accept_client(self):
        conn, addr = self.server_socket.accept()
        print(f"Connected to {addr}")

        # Send the public key to the client
        conn.send(self.public_key.export_key())
        print("Sent public key to client.")

        # Receive encrypted symmetric key
        encrypted_key = conn.recv(256)
        cipher_rsa = PKCS1_OAEP.new(self.private_key)
        symmetric_key = cipher_rsa.decrypt(encrypted_key).decode()

        # Receive encrypted message and decrypt it
        encrypted_message = conn.recv(1024).decode()
        decrypted_message = dna_decrypt_with_key(encrypted_message, symmetric_key)

        # Display decrypted message
        self.decrypted_msg_text.insert(END, decrypted_message)

        conn.close()
        self.server_socket.close()

if __name__ == "__main__":
    root = Tk()
    app = ServerApp(root)
    root.mainloop()
