def rot13(word):
    encrypted_word = ""
    for char in word:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            encrypted_char = char
        encrypted_word += encrypted_char
    return encrypted_word

if __name__ == "__main__":
    word = input("Ingrese una palabra: ")
    encrypted_word = rot13(word)
    print("Palabra encriptada:", encrypted_word)
