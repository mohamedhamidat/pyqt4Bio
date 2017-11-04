import unittest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')
from bio_formators import clean_format_sequence, format_to_string, format_gc_content

class TestBioFormators(unittest.TestCase):
    def test_clean_sequence(self):
        #Arrange
        sequence = ">TCAGg"   
        #Act
        clean_seq = clean_format_sequence(sequence)
        #Assert 
        self.assertEqual(clean_seq, "TCAGG")
    
    def test_format_to_string_when_message_is_dict(self):
        #Arrange
        key_values = {"1" : "ATGC", "2": "AAA"}   
        #Act
        string = format_to_string(key_values)
        #Assert 
        self.assertEqual(string, "1 ATGC\n2 AAA")

    def test_format_to_string_when_message_is_str(self):
        #Arrange
        message  = "ATG"  
        #Act
        string = format_to_string(message)
        #Assert 
        self.assertEqual(string, "ATG")

    def test_format_gc_contentr(self):
        #Arrange
        gc  = 0.5
        #Act
        string = format_gc_content(gc)
        #Assert 
        self.assertEqual(string, "GC = 50.0%")

def main():
    unittest.main()

if __name__ == '__main__':
    main()