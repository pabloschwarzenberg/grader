def cambiar(c):
    m="m"
    if ord(c) <= ord(m):
        return chr(ord(c)+13)
    else:
        return chr(ord(c)-13)
        
def rot13(palabra):
    resultado=""
    for i in range(len(palabra)):
        resultado += cambiar(palabra[i])
    return resultado


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           