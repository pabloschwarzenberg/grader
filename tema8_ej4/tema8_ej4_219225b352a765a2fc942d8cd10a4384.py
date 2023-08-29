def rot13(palabra):
    abc1 = "abcdefghijklm"
    abc2 = "nopqrstuvwxyz"
    copy=""
    i=0
    while i < len(palabra):
        if palabra[i] in abc1:
            copy += abc2[abc1.find(palabra[i])]
        else:
            copy += abc1[abc2.find(palabra[i])]
        i+=1
    return copy

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           