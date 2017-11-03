from itertools import takewhile

DNA_RNA_PAIRS = {"A" : "U", "C": "G", "G" : "C", "T" : "A"}

GENITIC_CODE= {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',}
    
def clean_sequence(sequence):
    if sequence.startswith(">"):
        sequence = sequence[1:]
    return sequence

def dna_to_rna(sequence):
    sequence = clean_sequence(sequence)
    return sequence.upper().replace('T', 'U')

def dna_to_protein(sequence):
    """
    return all possible protein (6 open frame)
    """
    sequence = clean_sequence(sequence)
    protein_sequence = []
    for frame in range(3): 
        codons = [sequence[i:i+3] for i in range(frame, len(sequence), 3)]
        coding_sequence  =  takewhile(lambda x: len(x) == 3 , codons)
        protein_sequence.append(''.join([GENITIC_CODE[codon] for codon in coding_sequence]))
    return protein_sequence