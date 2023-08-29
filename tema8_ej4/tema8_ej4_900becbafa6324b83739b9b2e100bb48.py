def rot13(palabra):
    resultado = ""
    for caracter in palabra:
        if caracter.isalpha():
            ascii_base = ord('a') if caracter.islower() else ord('A')
            desplazamiento = (ord(caracter) - ascii_base + 13) % 26
            nuevo_caracter = chr(ascii_base + desplazamiento)
            resultado += nuevo_caracter
        else:
            resultado += caracter

    return resultado

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print(f"Palabra encriptada:{palabra_encriptada}")
           