import unittest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')
from bio_convertors import dna_to_rna, dna_to_protein, reverse_complement

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
    
    def test_reverse_complement(self):
        #Arrange
        sequence = "TCAGG"   
        #Act
        seq_reversed = reverse_complement(sequence)
        #Assert 
        self.assertEqual(seq_reversed, "CCTGA")
        

def main():
    unittest.main()

if __name__ == "__main__":
    main()