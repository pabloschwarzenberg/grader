def rot13(palabra):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    root13 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
              'i', 'j', 'k', 'l', 'm']
    a = 0
    b = 0
    pF = ''
    palabra = list(palabra)
    while b < len(palabra):
        if a == 26:
            a = 0
        if palabra[b] == abc[a]:
            palabra[b] = root13[a]
            b += 1
            a += 1
        else:
            a += 1


    for e in palabra:
        pF += e

    return pF
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)

           