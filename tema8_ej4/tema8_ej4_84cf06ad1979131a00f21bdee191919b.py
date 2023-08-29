abc="abcdefghijklmnopkrstuvwxyz"
def rot13(palabra):
    cifradoDetexTo=""
    for i in palabra:
        Sustraccion = abc.find(i)+13
        Movim=int(Sustraccion)%len(abc)
        cifradoDetexTo = cifradoDetexTo + str(abc[Movim])
    return cifradoDetexTo
    
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
    