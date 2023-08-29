def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            if letra.islower():
                base = ord('a')
            else:
                base = ord('A')
            offset = (ord(letra) - base + 13) % 26
            resultado += chr(base + offset)
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
      