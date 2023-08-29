abc = "abcdefghijklmnopqrstuvwxyz"
def rot13(palabra):
    text=""
    for i in palabra:
        su=abc.find(i)+13
        m=int(su)%len(abc)
        text=text+str(abc[m])
    return text

mensaje = "hola"
print(rot13(mensaje))


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           