def rot13(word):
    encrypted_word = ''
    for char in word:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            encrypted_word += encrypted_char
        else:
            encrypted_word += char
    return encrypted_word


if __name__ == "__main__":
    # Ejemplo de uso
    palabra = input("Ingrese una palabra: ")
    resultado = rot13(palabra)
    print("Palabra encriptada:", resultado)
