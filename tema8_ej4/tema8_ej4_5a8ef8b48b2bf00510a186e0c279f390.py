import codecs
def rot13(palabra):
    mensaje = codecs.encode(palabra, "rot13")
    return mensaje