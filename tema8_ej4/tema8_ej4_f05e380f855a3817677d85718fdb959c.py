def rot13(palabra):
    text=""
    for i in palabra:
        suma=abc.find(i)+13
        m=int(suma)%len(abc)
        text=text + str(abc[m])
    return text

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
abc = "abcdefghijklmnopqrstuvwxyz"
