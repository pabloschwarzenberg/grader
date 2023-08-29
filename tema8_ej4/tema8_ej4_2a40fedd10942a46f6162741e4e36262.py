def rot13(palabra):
    encrypted_word = ""
    for char in palabra:
        if char.isalpha():
            ascii_value = ord(char)
            if char.islower():
                encrypted_value = (ascii_value - 97 + 13) % 26 + 97
            else:
                encrypted_value = (ascii_value - 65 + 13) % 26 + 65
            encrypted_word += chr(encrypted_value)
        else:
            encrypted_word += char
    return encrypted_word

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
           