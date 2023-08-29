def rot13(palabra):
    lista1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    lista2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    s=list(palabra)
    nuevo=""
    for i in s:
        if i in lista1:
            x=lista1.index(i)
            nuevo+=lista2[x]
        elif i in lista2:
            y=lista2.index(i)
            nuevo+=lista1[y]
    return nuevo
            

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           