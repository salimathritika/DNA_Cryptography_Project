
encoding_table = {
    'A': 'AACC', 'B': 'AAGG', 'C': 'TAAT', 'D': 'TATG', 'E': 'TACC',
    'F': 'TAGA', 'G': 'CAAT', 'H': 'CATG', 'I': 'CACG', 'J': 'CAGT',
    'K': 'GAAG', 'L': 'GATA', 'M': 'GACG', 'N': 'GAGG', 'O': 'AATA',
    'P': 'AACG', 'Q': 'TATC', 'R': 'TACG', 'S': 'CATC', 'T': 'CACC',
    'U': 'GATT', 'V': 'GACC', 'W': 'ATAA', 'X': 'ATTT', 'Y': 'ATCG',
    'Z': 'ATGC', ' ': 'GGGG', '.': 'ATCC', ',': 'ATTA', '?': 'TTTA',
    '0': 'TTAA', '1': 'TTTT', '2': 'TTCC', '3': 'TTGG', '4': 'CTAT',
    '5': 'CTTG', '6': 'CTCC', '7': 'CTGA', '8': 'GTAT', '9': 'GTTG'
}

# Reverse table: maps DNA sequences back to their characters, including numbers
reverse_table = {v: k for k, v in encoding_table.items()}


def encode_to_dna(plaintext, encoding_table):
    #Encodes a given plaintext string into a DNA sequence using the provided encoding table.
    dna_sequence = ''.join([encoding_table[char] for char in plaintext.upper() if char in encoding_table])
    return dna_sequence


def decode_from_dna(dna_sequence, reverse_table):
    #Decodes a DNA sequence back into plaintext using the provided reverse table.

    # Split the DNA sequence into chunks of 4
    chunks = [dna_sequence[i:i + 4] for i in range(0, len(dna_sequence), 4)]

    # If any chunk is less than 4 nucleotides, pad it with 'A'
    if len(chunks[-1]) < 4:
        chunks[-1] = chunks[-1].ljust(4, 'A')  # Ensures every chunk is of length 4

    # Decode the DNA sequence back to text
    plaintext = ''.join([reverse_table.get(chunk, '?') for chunk in chunks])

    return plaintext
