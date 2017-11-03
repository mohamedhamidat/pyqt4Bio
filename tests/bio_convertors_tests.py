import unittest
import sys
sys.path.insert(0, "../src")
from bio_convertors import dna_to_rna, dna_to_protein, clean_sequence, reverse_complement

class Bio_convertorsTests(unittest.TestCase):

    def test_dna_to_rna(self):
        #Arrange
        sequence = "ACGT"   
        #Act
        rna = dna_to_rna(sequence)
        #Assert 
        self.assertEqual(rna, "ACGU")
    
    def test_dna_to_protein(self): 
        #Arrange
        sequence = "TCAGG"   
        #Act
        protein = dna_to_protein(sequence)
        #Assert 
        self.assertEqual(protein[0], "S")

    def test_clean_sequence(self):
        #Arrange
        sequence = ">TCAGG"   
        #Act
        clean_seq = clean_sequence(sequence)
        #Assert 
        self.assertEqual(clean_seq, "TCAGG")
    
    def test_reverse_complement(self):
        #Arrange
        sequence = ">TCAGG"   
        #Act
        seq_reversed = reverse_complement(sequence)
        #Assert 
        self.assertEqual(seq_reversed, "CCTGA")
        

def main():
    unittest.main()

if __name__ == "__main__":
    main()