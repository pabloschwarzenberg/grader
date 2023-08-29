import codecs

def rot13(word):
    encoded_word = codecs.encode(word, 'rot_13')
    return encoded_word

if __name__ == "__main__":
    word = input("Ingrese una palabra: ")
    encrypted_word = rot13(word)
    print("Palabra encriptada:", encrypted_word)