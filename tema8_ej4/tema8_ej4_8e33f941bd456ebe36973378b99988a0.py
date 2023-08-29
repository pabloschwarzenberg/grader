def rot13(word):
    encrypted_word = ""
    for char in word:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
            encrypted_word += encrypted_char
        else:
            encrypted_word += char
    return encrypted_word
if __name__ == "__main__":
    word = input("Ingrese una palabra: ")
    encrypted_word = rot13(word)
    print("Palabra encriptada:", encrypted_word)