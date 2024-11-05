#for testing purposes

from dna_encrypt import dna_encrypt_with_key
from dna_decrypt import dna_decrypt_with_key
from key_generation import generate_dynamic_key
import random
from dna_encoding import encode_to_dna, encoding_table,decode_from_dna, reverse_table

key=generate_dynamic_key(random.randint(4,100))
round=random.randint(1,50)


def encrypt_text(pt):
    global flag
    flag=0
    if len(pt)%2==0:
        pt=pt+'x'
        flag=1
    dna_seq = encode_to_dna(pt, encoding_table)
    enc=dna_seq
    enc = dna_encrypt_with_key(enc, key,round)
    return enc

def decrypt_dna(ct):
    dec = dna_decrypt_with_key(ct, key,round)
    dec = decode_from_dna(dec, reverse_table)
    if flag==1:
        dec = dec[:len(dec)-1]
    return dec

pt=input("Enter plaintext:")
ct=encrypt_text(pt)
print("Encrypted message:",ct)
ct=input("Enter the DNA to be decrypted:")
dec=decrypt_dna(ct)
print("Decrypted DNA:",dec)

