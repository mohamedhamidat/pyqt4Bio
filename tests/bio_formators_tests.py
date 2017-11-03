import unittest
import sys
sys.path.insert(0, "../src")

from bio_formators import clean_format_sequence

class Bio_formatorsTests(unittest.TestCase):
    def test_clean_sequence(self):
        #Arrange
        sequence = ">TCAGg"   
        #Act
        clean_seq = clean_format_sequence(sequence)
        #Assert 
        self.assertEqual(clean_seq, "TCAGG")

def main():
    unittest.main()

if __name__ == '__main__':
    main()