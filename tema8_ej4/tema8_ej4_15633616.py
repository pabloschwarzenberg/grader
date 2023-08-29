def rot13(palabra):
    lista=list(palabra)
    listaa=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    listab=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    nueva=[]
    for i in lista:
        if i in listaa:
            x=listaa.index(i)
            j=listab[x]
            nueva.append(j)
        if i in listab:
            x=listab.index(i)
            j=listaa[x]
            nueva.append(j)
    palabra="".join(nueva)
    
    return palabra

    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           