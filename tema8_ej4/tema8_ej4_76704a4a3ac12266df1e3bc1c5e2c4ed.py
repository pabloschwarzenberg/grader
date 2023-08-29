def rot13(palabra):
    a=palabra.lower()
    lista1="abcdefghijklm"
    lista2="nopqrstuvwxyz"
    c=list(a)
    
    for i in range(len(c)):
        if lista1.count(c[i])==1:
            t=lista1.index(c[i])
            c[i]=lista2[t]
        elif lista2.count(c[i])==1:
            t=lista2.index(c[i])
            c[i]=lista1[t]
    b="".join(c)
    return b
  


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           