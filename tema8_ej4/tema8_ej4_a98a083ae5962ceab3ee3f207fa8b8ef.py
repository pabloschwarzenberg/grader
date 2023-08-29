def rot13(palabra):
    abc="abcdefghijklmnopqrstuvwxyzabcdefghijklm"
    abc=list(abc)
    palabralista=list(palabra)
    i=0
    while i<len(palabralista):
        x=palabralista[i]
        p=abc.index(x)+13
        palabralista[i]=abc[p]
        i+=1
    palabrafinal="".join(palabralista)
    return(palabrafinal)


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           