# dna_encoding.py
# DNA encoding and decoding using base pairs for encryption and decryption

# Encoding table: maps characters to their DNA representations
encoding_table = {
    'A': 'GACT', 'B': 'CGTA', 'C': 'TGCA', 'D': 'ATGC', 'E': 'CTGA',
    'F': 'GATC', 'G': 'AGCT', 'H': 'TCGA', 'I': 'GTCA', 'J': 'CAGT',
    'K': 'TACG', 'L': 'ACTG', 'M': 'TGAC', 'N': 'CAGC', 'O': 'TGCG',
    'P': 'GCTA', 'Q': 'GTAT', 'R': 'CGAC', 'S': 'ACGT', 'T': 'CTAG',
    'U': 'TCTA', 'V': 'TCCG', 'W': 'CGTG', 'X': 'GCAT', 'Y': 'ACGA',
    'Z': 'TAGC', ' ': 'GGGG', '.': 'AAAA', ',': 'CCCC', '?': 'TTTT',
}

# Reverse table: maps DNA sequences back to their characters
reverse_table = {v: k for k, v in encoding_table.items()}


def encode_to_dna(plaintext, encoding_table):
    dna_sequence = ''.join([encoding_table[char] for char in plaintext.upper()])
    return dna_sequence


def decode_from_dna(dna_sequence, reverse_table):
    # Split the DNA sequence into chunks of 4
    chunks = [dna_sequence[i:i + 4] for i in range(0, len(dna_sequence), 4)]

    # If any chunk is less than 4 nucleotides, pad it with 'A'
    if len(chunks[-1]) < 4:
        chunks[-1] = chunks[-1].ljust(4, 'A')  # Ensures every chunk is of length 4

    # Decode the DNA sequence back to text
    plaintext = ''.join([reverse_table.get(chunk, '?') for chunk in chunks])

    return plaintext
