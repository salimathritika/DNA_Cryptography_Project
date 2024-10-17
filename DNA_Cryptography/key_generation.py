import random

# Generate a dynamic key based on the length of the DNA sequence
def generate_dynamic_key(length):
    bases = ['A', 'T', 'C', 'G']
    return ''.join(random.choices(bases, k=length))
