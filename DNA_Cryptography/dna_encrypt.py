import random


def insert_introns(dna_sequence, intron_length=4):
    """
    Inserts introns randomly in the DNA sequence at specific positions to obfuscate the data.
    Introns are inserted symmetrically in the middle.
    """
    half_len = len(dna_sequence) // 2
    bases = ['A', 'T', 'C', 'G']

    # Create an intron sequence of the specified length
    intron_sequence = ''.join(random.choices(bases, k=intron_length))

    # Insert introns in the middle of the DNA sequence
    return dna_sequence[:half_len] + intron_sequence + dna_sequence[half_len:]


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


def dna_encrypt_with_key(dna_sequence, key='ACGT'):
    """
    XOR-based encryption with the DNA sequence using a repeating key.
    """
    encrypted_dna = []
    for i in range(len(dna_sequence)):
        key_base = key[i % len(key)]
        encrypted_base = dna_xor(dna_sequence[i], key_base)
        encrypted_dna.append(encrypted_base)

    encrypted_dna = ''.join(encrypted_dna)

    # Insert introns after the XOR encryption
    return insert_introns(encrypted_dna)


def dna_decrypt_with_key(dna_sequence, key='ACGT'):
    """
    XOR-based decryption for the encrypted DNA sequence using the key.
    Introns are removed before decryption.
    """
    # Remove introns before starting the decryption
    dna_sequence = remove_introns(dna_sequence)

    decrypted_dna = []
    for i in range(len(dna_sequence)):
        key_base = key[i % len(key)]
        decrypted_base = dna_xor(dna_sequence[i], key_base)
        decrypted_dna.append(decrypted_base)

    return ''.join(decrypted_dna)
