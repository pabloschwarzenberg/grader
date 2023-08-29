def rot13(palabra):
    l = list(palabra)
    abc = 'abcdefghijklmnopqrstuvwxyz'
    a = 0
    for i in palabra:
        if abc.find(i) <= 12:
            l[a] = abc[abc.find(i) + 13]
            a += 1
        else:
            l[a] = abc[abc.find(i) - 13]
            a += 1
    palabra = ''.join(l)
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           