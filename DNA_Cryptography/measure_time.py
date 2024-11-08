#for AES
from Crypto.Cipher import AES
from binascii import unhexlify, hexlify
from Crypto.Util.Padding import pad, unpad

#for DNA cryptography
from dna_encrypt import dna_encrypt_with_key
from dna_decrypt import dna_decrypt_with_key
from key_generation import generate_dynamic_key
import random
from dna_encoding import encode_to_dna, encoding_table,decode_from_dna, reverse_table

import time

key=generate_dynamic_key(random.randint(4,100))
round=16

def aes_encrypt(pt, key):
    start=time.perf_counter()
    aes = AES.new(key, AES.MODE_ECB)
    pad_text = pad(pt.encode(), AES.block_size)  # Corrected the encode call
    aes_ct = aes.encrypt(pad_text)
    stop=time.perf_counter()-start
    return hexlify(aes_ct).decode(), stop

def aes_decrypt(ct, key):
    start = time.perf_counter()
    aes = AES.new(key, AES.MODE_ECB)
    enc_bytes = unhexlify(ct)
    aes_dec = unpad(aes.decrypt(enc_bytes), AES.block_size)
    stop = time.perf_counter() - start
    return aes_dec.decode(), stop

def dna_encrypt(pt):
    start = time.perf_counter()
    global flag
    flag=0
    if len(pt)%2==0:
        pt=pt+'x'
        flag=1
    dna_seq = encode_to_dna(pt, encoding_table)
    enc=dna_seq
    enc = dna_encrypt_with_key(enc, key,round)
    stop = time.perf_counter() - start
    return enc, stop

def dna_decrypt(ct):
    start=time.perf_counter()
    dec = dna_decrypt_with_key(ct, key,round)
    dec = decode_from_dna(dec, reverse_table)
    if flag==1:
        dec = dec[:len(dec)-1]
    stop = time.perf_counter() - start
    return dec, stop

aes_key = unhexlify("0123456789ABCDEF0123456789ABCDEF")
pt=input("Enter a plaintext: ")
ct,aes_enc=aes_encrypt(pt, aes_key)
dec,aes_dec=aes_decrypt(ct,aes_key)

ct,dna_enc=dna_encrypt(pt)
dna_dec,dna_dec=dna_decrypt(ct)

print(f"AES Encryption time:{aes_enc}")
print(f"AES Decryption time:{aes_dec}")
print(f"DNA Encryption time:{dna_enc}")
print(f"DNA Decryption time:{dna_dec}")

