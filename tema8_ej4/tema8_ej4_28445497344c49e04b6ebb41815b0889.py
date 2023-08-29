def rot13(palabra):
    string="abcdefghijklmnopqrstuvwxyz"
    a=[]
    for letra in palabra:
        a.append(letra)
    for i in range(0,len(palabra)):
        b=string.find(a[i])
        c=(b+13)%26
        a[i]=string[c]
    return "".join(a)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           