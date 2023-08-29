letras="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
def rot13(palabra):
    c=len(palabra)
    d=[]
    while c>0:
        b=letras.find(palabra[c-1])
        a=letras[b+13]
        d.append(a)
        c=c-1
        s=list(reversed(d))
    return("".join(s))

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra=palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           