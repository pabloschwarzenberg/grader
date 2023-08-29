def rot13(palabra):
    abc="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    for i in range(0,len(palabra)):
        m=list(palabra)
        q=abc.find(palabra[i])
        m[i]=abc[q+13]
        t="".join(m)
        palabra=t
    return t

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)