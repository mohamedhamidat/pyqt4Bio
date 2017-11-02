DNA_RNA_PAIRS = {"A" : "U", "C": "G", "G" : "C", "T" : "A"}
def dna_to_rna(sequence):
    if sequence.startswith(">"):
        sequence = sequence[1:]
    return sequence.upper().replace('U', 'T')
    