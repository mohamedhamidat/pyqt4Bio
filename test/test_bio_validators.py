import unittest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')
from bio_validators  import is_valid_dna

class TestBiovalidators(unittest.TestCase):
    
    def test_is_valid_dna_should_raise_ValueErrorException_when_string_is_empty(self):
        with self.assertRaises(ValueError) as error:
            is_valid_dna("")
        self.assertEqual(error.exception.args[0], 'sequence should not be null or empty')
    
    def test_is_valid_dna_should_pairs_raise_ValueErrorException_when_string_isnot_valid(self):
        with self.assertRaises(ValueError) as error:
           is_valid_dna(123)
        self.assertEqual(error.exception.args[0], 'sequence has to be a valid string')

    def test_is_valid_dna_should_pairs_raise_ValueErrorException_when_superior_sign_missing(self):
        with self.assertRaises(ValueError) as error:
           is_valid_dna("AGCT")
        self.assertEqual(error.exception.args[0], 'sequence should start with >')
    
    def test_is_valid_dna_should_pairs_raise_ValueErrorException_when_seq_contains_invalid_base(self):
        with self.assertRaises(ValueError) as error:
           is_valid_dna(">AGCn")
        self.assertEqual(error.exception.args[0], 'sequence must have valid base')
    
    def test_is_valid_dna(self):
        # Arrange
        sequence = ">AGTC"
        # Act 
        result = is_valid_dna(sequence)
        #Assert
        self.assertEqual(result, True)

def main():
    unittest.main()

if __name__ == "__main__":
    main()