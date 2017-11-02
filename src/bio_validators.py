
DNA_BASES = ["A", "C", "G", "T"]

def dna(sequence):
    """
    if sequence is not a string: 
         raise ValueError("sequence has to be a valid string")
    
    if sequence is empty or null: 
         raise ValueError("sequence should not be null or empty")
    
    if sequence doesn't start with ">": 
        raise ValueError("sequence should start with >")
    
    if sequence doesn't contain valid ATGC base: 
        raise ValueError("sequence must have valid base")
    """
    if type(sequence) != str: 
         raise ValueError("sequence has to be a valid string")
    
    if not sequence: 
         raise ValueError("sequence should not be null or empty")
    
    if not sequence.startswith(">"): 
        raise ValueError("sequence should start with >")
    
    for base in sequence[1:].upper():
        if base not in DNA_BASES:
            raise ValueError("sequence must have valid base")
    
    return True