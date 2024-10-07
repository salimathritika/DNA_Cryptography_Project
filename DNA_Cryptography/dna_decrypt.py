# dna_decrypt.py
import random
from biological_processes import transcription, translation, reverse_transcription
from key_generation import generate_dynamic_key


# Remove introns from the DNA sequence during decryption
def remove_introns(dna_sequence, intron_length=4):
    # Simply removes the last `intron_length` bases
    return dna_sequence[:-intron_length]


def xor_dna(dna_sequence, key):
    dna_to_bin = {'A': '00', 'T': '01', 'C': '10', 'G': '11'}
    bin_to_dna = {v: k for k, v in dna_to_bin.items()}

    dna_bin = ''.join([dna_to_bin[base] for base in dna_sequence])
    key_bin = ''.join([dna_to_bin[base] for base in key])

    # XOR operation between DNA binary and key binary
    decrypted_bin = ''.join(['1' if dna_bin[i] != key_bin[i] else '0' for i in range(len(dna_bin))])

    # Convert back to DNA
    decrypted_dna = ''.join([bin_to_dna[decrypted_bin[i:i + 2]] for i in range(0, len(decrypted_bin), 2)])
    return decrypted_dna


# Decrypt DNA with intron removal and key XOR
def dna_decrypt_with_key(encrypted_dna, num_rounds=5):
    # Remove intron sequences
    encrypted_dna = remove_introns(encrypted_dna)

    # Generate the same dynamic key used for encryption
    key = generate_dynamic_key(len(encrypted_dna))

    # Reverse multi-round decryption process
    for _ in range(num_rounds):
        # Reverse right shift
        encrypted_dna = shift_left(encrypted_dna)

        # Reverse biological processes
        tRNA_sequence = transcription(encrypted_dna)
        mRNA_sequence = translation(tRNA_sequence)
        encrypted_dna = reverse_transcription(mRNA_sequence)

        # XOR with the same key to decrypt
        encrypted_dna = xor_dna(encrypted_dna, key)

    return encrypted_dna


# Shift left function for reverse of the shift right in encryption
def shift_left(dna_sequence):
    return dna_sequence[1:] + dna_sequence[0]
