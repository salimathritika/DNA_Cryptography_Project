DNA Cryptography Project

This project demonstrates a cryptographic method that mimics biological processes in DNA sequences, encoding and decoding data using DNA-like sequences. The approach incorporates XOR-based encryption, transcription, translation, and intron insertion for enhanced data security.

Project Structure

- dna_encrypt.py: Contains the encryption functions, including intron insertion, XOR encryption, transcription, and translation.
- dna_decrypt.py: Contains the decryption functions, including intron removal, reverse transcription, and XOR decryption.
- dna_encoding.py: Contains encoding and decoding tables and functions that map characters to DNA-like sequences.
- biological_processes.py: Contains additional biological processes such as transcription, translation, and reverse transcription.
- key_generation.py: Contains a function to generate dynamic keys based on DNA bases.
- gui.py: Provides a simple graphical interface for encrypting and decrypting messages.

Usage

Command Line Usage

1. Encryption:
   - Use the dna_encrypt_with_key() function from dna_encrypt.py to encrypt a plaintext message.
   - Example:
     from dna_encrypt import dna_encrypt_with_key
     key = 'ACGT'
     plaintext = 'HELLO'
     encrypted_dna = dna_encrypt_with_key(plaintext, key)
     print("Encrypted DNA:", encrypted_dna)
     

2. Decryption:
   - Use the dna_decrypt_with_key() function from dna_decrypt.py to decrypt an encrypted DNA sequence.
   - Example:
     from dna_decrypt import dna_decrypt_with_key
     decrypted_text = dna_decrypt_with_key(encrypted_dna, key)
     print("Decrypted Text:", decrypted_text)

GUI Usage

1. Run the GUI application:
   python gui.py
   
2. The GUI allows you to:
   - Enter plaintext to encrypt, with the encrypted DNA sequence displayed.
   - Enter an encrypted DNA sequence to decrypt, with the original plaintext displayed.

How It Works

1. Encoding and XOR Encryption
- Encoding: The plaintext is first encoded into a DNA-like sequence using a character-to-DNA mapping.
- XOR Encryption: Each base in the DNA sequence is XOR-ed with a repeating key to obfuscate the data.

2. Transcription and Translation
- Transcription: The encrypted DNA is transcribed to mRNA by replacing 'T' with 'U'.
- Translation: The mRNA is then translated into tRNA by finding complementary bases.

3. Intron Insertion
- Introns, or non-coding sequences, are randomly inserted in the middle of the tRNA sequence for further obfuscation.

4. Decryption Process
The decryption reverses these steps:
- Intron Removal: Removes introns to restore the original sequence.
- Reverse Transcription: Converts tRNA back to mRNA by replacing 'U' with 'T'.
- XOR Decryption: Uses the key to XOR the DNA back to the original sequence.
- Decoding: The decrypted DNA sequence is then decoded back to the original plaintext.

Example

Suppose the plaintext is "HELLO" and the key is "ACGT". Here’s how the encryption process works:

1. Encoding: "HELLO" is converted to a DNA sequence.
2. XOR Encryption: Each DNA base is XOR-ed with a corresponding base from the key.
3. Transcription: The XOR-ed DNA is converted to mRNA.
4. Translation: mRNA is translated to tRNA.
5. Intron Insertion: Random introns are inserted in the middle of the tRNA sequence.

During decryption, the steps are reversed to recover the original message.

Notes

- Ensure that the same key is used for both encryption and decryption.
- This project is experimental and intended for educational purposes, as DNA encryption is complex and requires advanced techniques for practical cryptographic use.
