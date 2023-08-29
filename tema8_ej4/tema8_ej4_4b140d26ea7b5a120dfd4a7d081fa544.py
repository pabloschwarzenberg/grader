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
            if caracter.isupper():
                codigo = ord(caracter) - 65
                nuevo_codigo = (codigo + 13) % 26 + 65
                resultado += chr(nuevo_codigo)
            else:
                codigo = ord(caracter) - 97
                nuevo_codigo = (codigo + 13) % 26 + 97
                resultado += chr(nuevo_codigo)
        else:
            resultado += caracter
    return resultado

if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es:", resultado)          