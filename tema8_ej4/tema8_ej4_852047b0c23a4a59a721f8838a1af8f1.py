def rot13(palabra):
    resultado = ''
    for caracter in palabra:
        if caracter.isalpha():
            if caracter.isupper():
                codigo = ord(caracter) - ord('A')
                encriptado = (codigo + 13)%26 + ord('A')
                resultado += chr(encriptado)
            else:
                codigo = ord(caracter) - ord('a')
                encriptado = (codigo + 13)%26 + ord('a')
                resultado += chr(encriptado)
        else:
            resultado += caracter
    return resultado    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           