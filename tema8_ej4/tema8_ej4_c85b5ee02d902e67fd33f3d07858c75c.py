def rot13(palabra):
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
def rot13(palabra):
    resultado = ""
    for caracter in palabra:
        if caracter.isalpha():
            codigo = ord(caracter)
            offset = 65 if caracter.isupper() else 97
            encriptado = (codigo - offset + 13) % 26 + offset
            resultado += chr(encriptado)
        else:
            resultado += caracter
    return resultado
          