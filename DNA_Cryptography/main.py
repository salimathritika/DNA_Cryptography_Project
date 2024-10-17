#for testing purposes

from dna_encoding import encode_to_dna, decode_from_dna, encoding_table, reverse_table


def encrypt_text(pt):
    encrypted_dna = encode_to_dna(pt, encoding_table)
    return encrypted_dna

def decrypt_dna(ct):
    decrypted_dna=decode_from_dna(ct,reverse_table)
    return decrypted_dna

pt=input("Enter plaintext:")
ct=encrypt_text(pt)
print("Encrypted message:",ct)
ct=input("Enter the DNA to be decrypted:")
dec=decrypt_dna(ct)
print("Decrypted DNA:",dec)

