def rot13(palabra):
    caracteres = "abcdefghijklmnopqrstuvwxyz"
    trans = caracteres[13:]+caracteres[:13]
    a_caracteres = lambda c: trans[caracteres.find(c)] if caracteres.find(c)>-1 else c
    return ''.join( a_caracteres(c) for c in palabra )

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           