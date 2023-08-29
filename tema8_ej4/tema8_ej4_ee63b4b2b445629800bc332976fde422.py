def rot13(palabra):
    
    if palabra == palabra.upper():
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        alfabeto = "abcdefghijklmnopqrstuvwxyz"

    cifrado = ""
    numero = 13

    for i in palabra:
        if i in alfabeto:
            cifrado = cifrado + alfabeto[(alfabeto.index(i) + numero) % (len(alfabeto))]
        else:
            cifrado = cifrado + i
    return cifrado


if __name__ == "__main__":
    x = input("ingrese la palabra que quieras encriptar  :")
    print (rot13(x))
    pass