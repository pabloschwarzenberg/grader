def rot13(palabra):
    palabra1=list(palabra)
    for i in range(len(palabra1)):
        letra=palabra1[i].lower()
        n1=ord(letra)
        if n1<=109:
            n2=chr(n1+13)
            palabra1[i]=n2
        elif 109<n1<123:
            n3=chr(n1-13)
            palabra1[i]=n3
    return "".join(palabra1)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)