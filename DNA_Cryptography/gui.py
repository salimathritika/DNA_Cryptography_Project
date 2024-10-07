import tkinter as tk
from dna_encoding import encode_to_dna, decode_from_dna, encoding_table, reverse_table

# Define the GUI
def create_gui():
    window = tk.Tk()
    window.title("Enhanced DNA Cryptography")

    # Input field for plaintext or DNA
    tk.Label(window, text="Enter Plaintext (for encryption) or Encrypted DNA (for decryption):").pack()
    input_field = tk.Entry(window, width=60)
    input_field.pack()

    # Result display (Text widget for easier copying)
    result_label = tk.Label(window, text="Result:")
    result_label.pack()
    result_display = tk.Text(window, height=2, width=40, wrap='word')
    result_display.pack()

    # Function to encrypt the input text
    def encrypt_text():
        plaintext = input_field.get()
        if plaintext:
            encrypted_dna = encode_to_dna(plaintext, encoding_table)
            result_display.delete('1.0', tk.END)
            result_display.insert(tk.END, encrypted_dna)

    # Function to decrypt the input DNA
    def decrypt_text():
        encrypted_dna = input_field.get()
        if encrypted_dna:
            decrypted_text = decode_from_dna(encrypted_dna, reverse_table)
            result_display.delete('1.0', tk.END)
            result_display.insert(tk.END, decrypted_text)

    # Buttons for encryption and decryption
    encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_text)
    encrypt_button.pack(side=tk.LEFT, padx=20)

    decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_text)
    decrypt_button.pack(side=tk.RIGHT, padx=20)

    window.mainloop()

# Run the GUI
if __name__ == "__main__":
    create_gui()
