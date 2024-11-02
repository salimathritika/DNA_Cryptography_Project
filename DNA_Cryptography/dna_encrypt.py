import random
from dna_encoding import encode_to_dna, encoding_table
from biological_processes import transcription



def insert_introns(dna_sequence, intron_length=4):
    #Inserts introns randomly in the DNA sequence at specific positions to obfuscate the data.
    #Introns are inserted symmetrically in the middle.
    
    half_len = len(dna_sequence) // 2
    bases = ['A', 'T', 'C', 'G']

    # Create an intron sequence of the specified length
    intron_sequence = ''.join(random.choices(bases, k=intron_length))

    # Insert introns in the middle of the DNA sequence
    return dna_sequence[:half_len] + intron_sequence + dna_sequence[half_len:]


def dna_xor(base1, base2):
    #XOR of two given DNA bases
    xor_table = {
        ('A', 'A'): 'A', ('A', 'C'): 'C', ('A', 'G'): 'G', ('A', 'T'): 'T',
        ('C', 'A'): 'C', ('C', 'C'): 'A', ('C', 'G'): 'T', ('C', 'T'): 'G',
        ('G', 'A'): 'G', ('G', 'C'): 'T', ('G', 'G'): 'A', ('G', 'T'): 'C',
        ('T', 'A'): 'T', ('T', 'C'): 'G', ('T', 'G'): 'C', ('T', 'T'): 'A',
    }
    return xor_table[(base1, base2)]



def dna_encrypt_with_key(pt, key):
    #Encode plaintext into DNA sequence
    dna_sequence = encode_to_dna(pt, encoding_table)

    #XOR-based encryption
    encrypted_dna = []
    for i in range(len(dna_sequence)):
        key_base = key[i % len(key)]
        encrypted_base = dna_xor(dna_sequence[i], key_base)
        encrypted_dna.append(encrypted_base)

    encrypted_dna = ''.join(encrypted_dna)

    #Transcription (convert to mRNA)
    transcribed_dna = transcription(encrypted_dna)

    #Insert introns after transcription
    enc_dna = insert_introns(transcribed_dna)

    return enc_dna