def rot13(palabra):
    encrypted_word = ""
    for char in palabra:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_word += encrypted_char
    return encrypted_word

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
