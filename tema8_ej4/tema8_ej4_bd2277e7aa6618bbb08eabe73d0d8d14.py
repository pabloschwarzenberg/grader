def rot13(palabra):
    resultado = ''
    for caracter in palabra:
        if caracter.isalpha():
            if caracter.isupper():
                ascii_offset = ord('A')
            else:
                ascii_offset = ord('a')
            caracter_codificado = chr((ord(caracter) - ascii_offset + 13) % 26 + ascii_offset)
            resultado += caracter_codificado
        else:
            resultado += caracter
    return resultado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           