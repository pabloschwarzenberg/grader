def rot13(palabra):
    resultado = ""
    for char in palabra:
        if char.isalpha():
            if char.islower():
                ascii_code = (ord(char) - ord('a') + 13) % 26 + ord('a')
            else:
                ascii_code = (ord(char) - ord('A') + 13) % 26 + ord('A')
            resultado += chr(ascii_code)
        else:
            resultado += char
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)
