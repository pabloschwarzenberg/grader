def rot13(palabra):
    y = 13
    x = ''
    if palabra == palabra.upper():
        l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    else:
        l = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    for i in palabra:
        if i in l:
            x+= l[l.index(i) + y%(len(l))]
        else:
            x+=i

    return x
    pass
if __name__ == "__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ", resultado)
