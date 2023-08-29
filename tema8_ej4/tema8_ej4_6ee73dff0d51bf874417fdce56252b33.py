def rot13(palabra):
    palabra=list(palabra)
    contador=0
    lista=[]
    if contador<=len(palabra):
        for i in palabra:
            if i=="a":
                letra="n"
                lista.append(letra)
            elif i=="b":
                letra="o"
                lista.append(letra)
            elif i=="c":
                letra="p"
                lista.append(letra)
            elif i=="d":
                letra="q"
                lista.append(letra)
            elif i=="e":
                letra="r"
                lista.append(letra)
            elif i=="f":
                letra="s"
                lista.append(letra)
            elif i=="g":
                letra="t"
                lista.append(letra)
            elif i=="h":
                letra="u"
                lista.append(letra)
            elif i=="i":
                letra="v"
                lista.append(letra)
            elif i=="j":
                letra="w"
                lista.append(letra)
            elif i=="k":
                letra="x"
                lista.append(letra)
            elif i=="l":
                letra="y"
                lista.append(letra)
            elif i=="m":
                letra="z"
                lista.append(letra)
            elif i=="n":
                letra="a"
                lista.append(letra)
            elif i=="o":
                letra="b"
                lista.append(letra)
            elif i=="p":
                letra="c"
                lista.append(letra)
            elif i=="q":
                letra="d"
                lista.append(letra)
            elif i=="r":
                letra="e"
                lista.append(letra)
            elif i=="s":
                letra="f"
                lista.append(letra)
            elif i=="t":
                letra="g"
                lista.append(letra)
            elif i=="u":
                letra="h"
                lista.append(letra)
            elif i=="v":
                letra="i"
                lista.append(letra)
            elif i=="w":
                letra="j"
                lista.append(letra)
            elif i=="x":
                letra="k"
                lista.append(letra)
            elif i=="y":
                letra="l"
                lista.append(letra)
            elif i=="z":
                letra="m"
                lista.append(letra)
        contador=contador+1
    resultado="".join(lista)
    return resultado


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)           