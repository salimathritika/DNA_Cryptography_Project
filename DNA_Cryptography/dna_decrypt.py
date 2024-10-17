import random
from biological_processes import reverse_transcription

def remove_introns(dna_sequence, intron_length=4):
    """
    Removes the introns inserted in the DNA sequence. Assumes they are in the middle.
    """
    half_len = len(dna_sequence) // 2
    return dna_sequence[:half_len] + dna_sequence[half_len + intron_length:]


def dna_xor(base1, base2):
    """
    XOR two DNA bases.
    """
    xor_table = {
        ('A', 'A'): 'A', ('A', 'C'): 'C', ('A', 'G'): 'G', ('A', 'T'): 'T',
        ('C', 'A'): 'C', ('C', 'C'): 'A', ('C', 'G'): 'T', ('C', 'T'): 'G',
        ('G', 'A'): 'G', ('G', 'C'): 'T', ('G', 'G'): 'A', ('G', 'T'): 'C',
        ('T', 'A'): 'T', ('T', 'C'): 'G', ('T', 'G'): 'C', ('T', 'T'): 'A',
    }
    return xor_table[(base1, base2)]


def dna_decrypt_with_key(dna_sequence,key):
    # XOR-based encryption with the DNA sequence using a repeating key.

    decrypted_dna = []
    for i in range(len(dna_sequence)):
        key_base = key[i % len(key)]
        decrypted_base = dna_xor(dna_sequence[i], key_base)
        decrypted_dna.append(decrypted_base)

    decrypted_dna = ''.join(decrypted_dna)

    dec_dna=remove_introns(decrypted_dna)
    #dec_dna=reverse_transcription(dec_dna)

    return dec_dna
