def rot13(palabra):
    a="abcdefghijklmnopqrstuvwxyz"
    palabro=""
    for letra in palabra:
        pos=0
        while letra != a[pos]:
            pos+=1
        if pos<13:
            j=pos+13
            palabro+=(a[j])
        if pos>=13:
            k=pos-13
            palabro+=(a[k])
    return palabro
        

if __name__=="__main__":
    palabra=str(input("Ingresa la palabra que quieras encriptar: "))
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)