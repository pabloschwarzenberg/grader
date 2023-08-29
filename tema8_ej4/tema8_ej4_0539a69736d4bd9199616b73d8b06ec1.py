def rot13(palabra):
    lista=("abcdefghijklmnopqrstuvwxyz")
    lista2=("nopqrstuvwxyzabcdefghijklm")
    pala=[]
    palabra_traducida=[]
    for i in palabra:
        pala.append(i)
    for i in pala:
        if i in " ":
            palabra_traducida.append(" ")
        else:
            a=lista.find(i)
            palabra_traducida.append(lista2[a])
    mi="".join(palabra_traducida)
    return(mi)
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           