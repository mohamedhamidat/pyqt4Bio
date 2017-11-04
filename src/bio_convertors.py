from itertools import takewhile

DNA_RNA_PAIRS = {"A" : "U", "C": "G", "G" : "C", "T" : "A"}
BASECOMPLEMENT = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
GENITIC_CODE = {
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

def dna_to_rna(sequence):
    """
    replace T base to U base 
    """
    return sequence.replace('T', 'U')

def gc_content(sequence):
    return float ((sequence.count('G') + sequence.count('C'))) / len(sequence)



def reverse_complement(sequence):
    """
    reverse sequence and complement base
    >>>reverse_complement(ATG)
    >>> CAT
    """
    reversed_seq = sequence[::-1]
    seq_reversed_complement = [BASECOMPLEMENT[base] for base in reversed_seq]
    return "".join(seq_reversed_complement)

def dna_to_protein(sequence):
    """
    return all possible protein (6 open frame) in frame: sequence pairs
    """
    sequences = [sequence, reverse_complement(sequence)]
    protein_sequence = {}
    frame_number = 0
    for seq in sequences: 
        protein_sequence[seq] =  ""
        for frame in range(3): 
            frame_number += 1
            codons = [seq[i:i+3] for i in range(frame, len(seq), 3)]
            coding_sequence  =  takewhile(lambda x: len(x) == 3 , codons)
            protein_sequence["frame %d:"%frame_number] = ''.join([GENITIC_CODE[codon] for codon in coding_sequence])
    return protein_sequence