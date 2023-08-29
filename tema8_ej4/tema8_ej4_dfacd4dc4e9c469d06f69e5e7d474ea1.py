def rot13(palabra):
    cod = []
    palabra = list(palabra)
    al_1='abcdefghijklmnopqrstuvwxyz'
    al_1=list(al_1)*2
    for i in palabra:
        cod += al_1[al_1.index(i) + 13]


    cod = ''.join(cod)
    return cod
    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           