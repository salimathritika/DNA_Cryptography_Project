import random
from dna_encoding import decode_from_dna, reverse_table
from biological_processes import reverse_transcription


def remove_introns(dna_sequence, intron_length=4):
    #Removes the introns
    half_len = len(dna_sequence) // 2
    return dna_sequence[:half_len] + dna_sequence[half_len + intron_length:]


def dna_xor(base1, base2):
    #XOR the DNA bases
    xor_table = {
        ('A', 'A'): 'A', ('A', 'C'): 'C', ('A', 'G'): 'G', ('A', 'T'): 'T',
        ('C', 'A'): 'C', ('C', 'C'): 'A', ('C', 'G'): 'T', ('C', 'T'): 'G',
        ('G', 'A'): 'G', ('G', 'C'): 'T', ('G', 'G'): 'A', ('G', 'T'): 'C',
        ('T', 'A'): 'T', ('T', 'C'): 'G', ('T', 'G'): 'C', ('T', 'T'): 'A',
    }
    return xor_table[(base1, base2)]



def dna_decrypt_with_key(dna_sequence, key):
    #Remove introns
    dna_sequence = remove_introns(dna_sequence)

    #Reverse transcription (convert mRNA back to DNA)
    reversed_dna = reverse_transcription(dna_sequence)

    #XOR-based decryption
    decrypted_dna = []
    for i in range(len(reversed_dna)):
        key_base = key[i % len(key)]
        decrypted_base = dna_xor(reversed_dna[i], key_base)
        decrypted_dna.append(decrypted_base)

    decrypted_dna = ''.join(decrypted_dna)

    #Decode decrypted DNA back to plaintext
    dec = decode_from_dna(decrypted_dna, reverse_table)
    
    return dec