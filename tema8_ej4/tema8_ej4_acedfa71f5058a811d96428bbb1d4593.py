def rot13(palabra):
    caracteres=list(palabra)
    palabrafinal=[]
    for letra in (caracteres):
        nuevocaracter=letra+13
        palabrafinal.append(nuevocaracter)
    return str(palabrafinal)
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           