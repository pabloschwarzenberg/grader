import codecs

def rot13(palabra):
    r = codecs.encode(palabra, 'rot_13')

    return r



