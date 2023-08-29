def rot13(palabra):
    resultado = ""
    
    for caracter in palabra:
        if caracter.isalpha():
            codigo = ord(caracter)
            if codigo >= 65 and codigo <= 90:  # Letra mayúscula
                nuevo_codigo = (codigo - 65 + 13) % 26 + 65
            elif codigo >= 97 and codigo <= 122:  # Letra minúscula
                nuevo_codigo = (codigo - 97 + 13) % 26 + 97
            nuevo_caracter = chr(nuevo_codigo)
            resultado += nuevo_caracter
        else:
            resultado += caracter
    
    return resultado

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada: ", palabra_encriptada)

           