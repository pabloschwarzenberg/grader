def rot13(palabra):
    enc=""
    for i in palabra:
        if ord(i)<=109 :
            j=chr(ord(i)+13)
            enc+=j
        if ord(i)>109:
            j=chr(ord(i)-13)
            enc+=j
    return enc

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           