import unittest
import sys
sys.path.insert(0, "../src")
from bio_convertors import dna_to_rna, dna_to_protein

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

def main():
    unittest.main()

if __name__ == "__main__":
    main()