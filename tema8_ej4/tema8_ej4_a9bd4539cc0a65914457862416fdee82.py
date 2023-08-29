def rot13(palabra):
    abc = "abcdefghijklmnopqrstuvwxyz"
    i = 13
    descifrado = ""
    for l in palabra:
        if l in abc:
            pos_letra = abc.index(l)
            nueva_pos = (pos_letra + i) % len(abc)
            descifrado += abc[nueva_pos]
        else:
            descifrado+= l
    msj = descifrado
    print(msj)
if __name__ == "__main__":
    palabra = input("ingrese su palabra para codificar")
    #pass