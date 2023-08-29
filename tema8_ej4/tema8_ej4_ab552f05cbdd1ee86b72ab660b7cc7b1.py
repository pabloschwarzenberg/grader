def rot13(palabra):
    lista=list(palabra)
    abc=list("abcdefghijklm")
    abc2=list("nopqrstuvwxyz")
    for i in range(0,len(lista)):
        if lista[i] in abc:
            lista[i]=abc2[abc.index(lista[i])]
        elif lista[i] in abc2:
            lista[i]=abc[abc2.index(lista[i])]
        string="".join(lista)
    return string
        
            
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    lista=list(palabra)
    abc=list("abcdefghijklm")
    abc2=list("nopqrstuvwxyz")
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)

