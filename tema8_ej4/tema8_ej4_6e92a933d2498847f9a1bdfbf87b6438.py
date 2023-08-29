def rot13(palabra):
    return ''.join([chr(97 + (((ord(i) - 97) + 13) % 26)) for i in palabra])

''' 
Version larga

def rot13(palabra):
    asc = [ord(i) - 97 for i in palabra]
    rot = [chr(97 + ((i + 13) % 26)) for i in asc]
    return ''.join(rot)
'''