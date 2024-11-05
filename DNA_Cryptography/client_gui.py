import socket
from tkinter import *
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from dna_encrypt import dna_encrypt_with_key
from key_generation import generate_dynamic_key
import random
from dna_encoding import encode_to_dna, encoding_table

round=16

def get_dynamic_key(length):
    key = generate_dynamic_key(random.randint(4, 100))
    return key


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
        symmetric_key = get_dynamic_key(4)
        cipher_rsa = PKCS1_OAEP.new(public_key)
        encrypted_key = cipher_rsa.encrypt(symmetric_key.encode())
        client_socket.send(encrypted_key)

        # Get plaintext, encrypt it, and display/send it
        plaintext = self.plaintext_entry.get()
       # encrypted_message = dna_encrypt_with_key(plaintext, symmetric_key)
        if len(plaintext) % 2 == 0:
            plaintext = plaintext + 'x'
            # flag=1
        dna_seq = encode_to_dna(plaintext, encoding_table)
        encrypted_message = dna_seq
        encrypted_message = dna_encrypt_with_key(encrypted_message, symmetric_key, round)

        # Insert encrypted message into the text box
        self.encrypted_msg_text.insert(END, encrypted_message)

        # Send the encrypted message to the server
        client_socket.send(encrypted_message.encode())

        client_socket.close()


if __name__ == "__main__":
    root = Tk()
    app = ClientApp(root)
    root.mainloop()
