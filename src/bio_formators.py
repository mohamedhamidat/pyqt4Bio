
def clean_format_sequence(sequence):
    """
    return sequence upper case and without > signe 
    """
    return sequence.replace('>', '').upper()

def format_to_string(message):
    if type (message) == dict: 
        return "\n".join([key + " " + value for key, value in message.items()])
    elif type(message) == str:
        return message
        
def format_gc_content(gc_content):
    return "GC = " + "{0:.2f}".format(gc_content * 100) + "%"