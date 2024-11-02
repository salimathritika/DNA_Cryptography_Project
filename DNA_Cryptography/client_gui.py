import socket
import random
from tkinter import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from dna_encrypt import dna_encrypt_with_key


def generate_dynamic_key(length):
    """Generate a dynamic key based on the length of the DNA sequence."""
    bases = ['A', 'T', 'C', 'G']
    return ''.join(random.choices(bases, k=length))


class ClientApp:
    def __init__(self, master):
        self.master = master
        self.master.title("DNA Cryptography Client")
        self.master.geometry("400x300")

        # GUI Components
        Label(master, text="Server Public Key:").pack()
        self.pubkey_text = Text(master, height=5, width=40)
        self.pubkey_text.pack()

        Label(master, text="Enter Plaintext:").pack()
        self.plaintext_entry = Entry(master, width=40)
        self.plaintext_entry.pack()

        Button(master, text="Send Encrypted Message", command=self.send_encrypted_message).pack()
        self.encrypted_label = Label(master, text="Encrypted Message:")
        self.encrypted_label.pack()
        self.encrypted_msg_text = Text(master, height=5, width=40)
        self.encrypted_msg_text.pack()

    def send_encrypted_message(self):
        # Clear the encrypted message box each time before encryption
        self.encrypted_msg_text.delete("1.0", END)

        # Connect to server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 12345))

        # Receive server's public key
        public_key_data = client_socket.recv(1024)
        public_key = RSA.import_key(public_key_data)
        self.pubkey_text.insert(END, public_key.export_key().decode())

        # Generate symmetric key and encrypt with server's public key
        symmetric_key = generate_dynamic_key(4)
        cipher_rsa = PKCS1_OAEP.new(public_key)
        encrypted_key = cipher_rsa.encrypt(symmetric_key.encode())
        client_socket.send(encrypted_key)

        # Get plaintext, encrypt it, and display/send it
        plaintext = self.plaintext_entry.get()
        encrypted_message = dna_encrypt_with_key(plaintext, symmetric_key)

        # Insert encrypted message into the text box
        self.encrypted_msg_text.insert(END, encrypted_message)

        # Send the encrypted message to the server
        client_socket.send(encrypted_message.encode())

        client_socket.close()


if __name__ == "__main__":
    root = Tk()
    app = ClientApp(root)
    root.mainloop()
