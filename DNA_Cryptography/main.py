#for testing purposes

from dna_encoding import encode_to_dna, decode_from_dna, encoding_table, reverse_table
from dna_encrypt import dna_encrypt_with_key
from dna_decrypt import dna_decrypt_with_key
from key_generation import generate_dynamic_key

key=generate_dynamic_key(4)

def encrypt_text(pt):
    dna_seq = encode_to_dna(pt, encoding_table)
    enc=dna_encrypt_with_key(dna_seq,key)
    return enc

def decrypt_dna(ct):
    dec_dna=dna_decrypt_with_key(ct,key)
    dec = decode_from_dna(dec_dna, reverse_table)
    return dec

pt=input("Enter plaintext:")
ct=encrypt_text(pt)
print("Encrypted message:",ct)
ct=input("Enter the DNA to be decrypted:")
dec=decrypt_dna(ct)
print("Decrypted DNA:",dec)

