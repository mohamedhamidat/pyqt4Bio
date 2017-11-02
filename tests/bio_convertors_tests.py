import unittest
import sys
sys.path.insert(0, "../src")
from bio_convertors import dna_to_rna

class Bio_convertorsTests(unittest.TestCase):

    def test_dna_to_rna(self):
        #Arrange
        sequence = "ACGT"   
        #Act
        rna = dna_to_rna(sequence)
        #Assert 
        self.assertEqual(rna, "ACGU")

def main():
    unittest.main()

if __name__ == "__main__":
    main()