import random
from dna_encoding import decode_from_dna, reverse_table
from biological_processes import reverse_transcription,translation, rev_translation


def remove_introns(dna_sequence, intron_length=4):
    #Removes the introns
    half_len = (len(dna_sequence)) // 2
    return dna_sequence[:half_len] + dna_sequence[half_len + intron_length:]


def dna_xor(base1, base2):
    #XOR the DNA bases
    """""
    xor_table = {
        ('A', 'A'): 'A', ('A', 'C'): 'C', ('A', 'G'): 'G', ('A', 'T'): 'T',
        ('C', 'A'): 'C', ('C', 'C'): 'A', ('C', 'G'): 'T', ('C', 'T'): 'G',
        ('G', 'A'): 'G', ('G', 'C'): 'T', ('G', 'G'): 'A', ('G', 'T'): 'C',
        ('T', 'A'): 'T', ('T', 'C'): 'G', ('T', 'G'): 'C', ('T', 'T'): 'A',
    }
    """
    xor_table = {
        ('A', 'A'): 'A', ('A', 'C'): 'C', ('A', 'G'): 'G', ('A', 'T'): 'T', ('A', 'U'): 'U',
        ('C', 'A'): 'C', ('C', 'C'): 'A', ('C', 'G'): 'T', ('C', 'T'): 'G', ('C', 'U'): 'U',
        ('G', 'A'): 'G', ('G', 'C'): 'T', ('G', 'G'): 'A', ('G', 'T'): 'C', ('G', 'U'): 'U',
        ('T', 'A'): 'T', ('T', 'C'): 'G', ('T', 'G'): 'C', ('T', 'T'): 'A', ('T', 'U'): 'U',
        ('U', 'A'): 'U', ('U', 'C'): 'U', ('U', 'G'): 'U', ('U', 'T'): 'U', ('U', 'U'): 'A'
    }

    return xor_table[(base1, base2)]

def shift_left(dna_sequence, shift_by):
    """
    Shifts the DNA sequence to the left by `shift_by` positions.
    """
    shift_by = shift_by % len(dna_sequence)  # To handle shifts greater than the sequence length
    return dna_sequence[shift_by:] + dna_sequence[:shift_by]

def dna_decrypt_with_key(dna_sequence, key,rounds):
    #Remove introns
    dna_sequence = remove_introns(dna_sequence)

    #translation
    dna_sequence=rev_translation(dna_sequence)

    #Reverse transcription (convert mRNA back to DNA)
    reversed_dna = reverse_transcription(dna_sequence)

    #DNA Sequence Shifting
    for j in range(rounds):
        reversed_dna = shift_left(reversed_dna, 1)

    #XOR-based decryption
    decrypted_dna=[]
    for i in range(len(reversed_dna)):
        key_base = key[i % len(key)]
        decrypted_base = dna_xor(reversed_dna[i], key_base)
        decrypted_dna.append(decrypted_base)

    dec = ''.join(decrypted_dna)

    
    return dec

