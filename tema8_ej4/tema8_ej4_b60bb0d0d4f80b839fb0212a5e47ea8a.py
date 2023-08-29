def rot13(palabra):
    resultado=""
    abc="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    for i in palabra:
        p=abc.find(i)
        f=p+13
        c=abc[f]
        resultado+=c
    return resultado
    pass
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es:",resultado)


           