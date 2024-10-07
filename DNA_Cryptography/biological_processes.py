# biological_processes.py
def transcription(dna_sequence):
    # Convert DNA sequence to mRNA (replace T with U)
    return dna_sequence.replace('T', 'U')

def translation(mRNA_sequence):
    # Convert mRNA to tRNA by finding complement (A->U, U->A, C->G, G->C)
    complements = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    tRNA_sequence = ''.join([complements[base] for base in mRNA_sequence])
    return tRNA_sequence

def reverse_transcription(tRNA_sequence):
    # Convert tRNA back to DNA (replace U with T)
    return tRNA_sequence.replace('U', 'T')
