def rot13(palabra):
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    encrip=''
    for i in palabra:
        if i in alfabeto:
            if alfabeto.index(i)<13:
                encrip+=alfabeto[alfabeto.index(i)+13]
            else:
                encrip+=alfabeto[alfabeto.index(i)-13]
    return encrip

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           