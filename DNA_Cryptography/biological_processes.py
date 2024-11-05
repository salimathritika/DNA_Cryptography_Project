
def transcription(dna_sequence):
    #Converts DNA sequence to mRNA by replacing T with U.
    return dna_sequence.replace('T', 'U')


def reverse_transcription(tRNA_sequence):
    #Converts mRNA (tRNA) back to DNA by replacing U with T.
    return tRNA_sequence.replace('U', 'T')

def translation(mRNA_sequence):
    # Convert mRNA to tRNA by finding complement (A->U, U->A, C->G, G->C)
    complements = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    tRNA_sequence = ''.join([complements[base] for base in mRNA_sequence])
    return tRNA_sequence