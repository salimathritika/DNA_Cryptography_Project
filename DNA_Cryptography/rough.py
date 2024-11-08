def shift_right(dna_sequence, shift_by):
    """
    Shifts the DNA sequence to the right by `shift_by` positions.
    """
    shift_by = shift_by % len(dna_sequence)  # To handle shifts greater than the sequence length
    return dna_sequence[-shift_by:] + dna_sequence[:-shift_by]

def shift_left(dna_sequence, shift_by):
    """
    Shifts the DNA sequence to the left by `shift_by` positions.
    """
    shift_by = shift_by % len(dna_sequence)  # To handle shifts greater than the sequence length
    return dna_sequence[shift_by:] + dna_sequence[:shift_by]

print(shift_left("ABCDEFG",1))