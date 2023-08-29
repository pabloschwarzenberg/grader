def rot13(palabra):
    caracteres = "abcdefghijklmnopqrstuvwxyz"
    llave = 13
    resultado = ""
    for caracter in palabra:
        if (caracteres.index(caracter) + llave)<=len(caracteres)-1:
            pos = (caracteres.index(caracter) + llave)
            resultado += caracteres[pos]
        if (caracteres.index(caracter) + llave)>len(caracteres)-1:
            pos = (caracteres.index(caracter) - llave)
            resultado += caracteres[pos]
    return resultado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           