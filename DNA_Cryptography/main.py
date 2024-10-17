#for testing purposes

from dna_encrypt import dna_encrypt_with_key
from dna_decrypt import dna_decrypt_with_key
from key_generation import generate_dynamic_key

key=generate_dynamic_key(4)

def encrypt_text(pt):
    enc=dna_encrypt_with_key(pt,key)
    return enc

def decrypt_dna(ct):
    dec=dna_decrypt_with_key(ct,key)
    return dec

pt=input("Enter plaintext:")
ct=encrypt_text(pt)
print("Encrypted message:",ct)
ct=input("Enter the DNA to be decrypted:")
dec=decrypt_dna(ct)
print("Decrypted DNA:",dec)

