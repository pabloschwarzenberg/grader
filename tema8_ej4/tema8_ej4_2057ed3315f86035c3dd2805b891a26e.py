def rot13(palabra):
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
def rot13(palabra):
    resultado = ""
    for letra in palabra:
        if letra.isalpha():
            codigo = ord(letra)
            if letra.islower():
                codigo_encriptado = (codigo - 97 + 13) % 26 + 97
            else:
                codigo_encriptado = (codigo - 65 + 13) % 26 + 65
            letra_encriptada = chr(codigo_encriptado)
            resultado += letra_encriptada
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa una palabra: ")
    palabra_encriptada = rot13(palabra)
    print("Palabra encriptada:", palabra_encriptada)
