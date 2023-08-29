def rot13(palabra):
    palabra_cifrada=""
    for letra in palabra:
        if letra=="a":
            palabra_cifrada+="n"
        elif letra=="b":
            palabra_cifrada+="o"
        elif letra=="c":
            palabra_cifrada+="p"
        elif letra=="d":
            palabra_cifrada+="q"
        elif letra=="e":
            palabra_cifrada+="r"
        elif letra=="f":
            palabra_cifrada+="s"
        elif letra=="g":
            palabra_cifrada+="t"
        elif letra=="h":
            palabra_cifrada+="u"
        elif letra=="i":
            palabra_cifrada+="v"
        elif letra=="j":
            palabra_cifrada+="w"
        elif letra=="k":
            palabra_cifrada+="x"
        elif letra=="l":
            palabra_cifrada+="y"
        elif letra=="m":
            palabra_cifrada+="z"
        elif letra=="n":
            palabra_cifrada+="a"
        elif letra=="o":
            palabra_cifrada+="b"
        elif letra=="p":
            palabra_cifrada+="c"
        elif letra=="q":
            palabra_cifrada+="d"
        elif letra=="r":
            palabra_cifrada+="e"
        elif letra=="s":
            palabra_cifrada+="f"
        elif letra=="t":
            palabra_cifrada+="g"
        elif letra=="u":
            palabra_cifrada+="h"
        elif letra=="v":
            palabra_cifrada+="i"
        elif letra=="w":
            palabra_cifrada+="j"
        elif letra=="x":
            palabra_cifrada+="k"
        elif letra=="y":
            palabra_cifrada+="l"
        elif letra=="z":
            palabra_cifrada+="m"
        

    return palabra_cifrada

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           