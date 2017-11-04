
def clean_format_sequence(sequence):
    """
    return sequence upper case and without > signe 
    """
    return sequence.replace('>', '').upper()

def dictionary_to_string(dictionary):
    return "n/".join([key + " " + value for key, value in dictionary.items()])
