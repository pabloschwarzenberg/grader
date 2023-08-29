def rot13(palabra):
    p=""
    for i in range (0, len(palabra)):
        if palabra[i]=="a":
            p+="n"
        elif palabra[i]=="b":
            p+="o"
        elif palabra[i]=="c":
            p+="p"
        elif palabra[i]=="d":
            p+="q"
        elif palabra[i]=="e":
            p+="r"
        elif palabra[i]=="f":
            p+="s"
        elif palabra[i]=="g":
            p+="t"
        elif palabra[i]=="h":
            p+="u"
        elif palabra[i]=="i":
            p+="v"
        elif palabra[i]=="j":
            p+="w"
        elif palabra[i]=="k":
            p+="x"
        elif palabra[i]=="l":
            p+="y"
        elif palabra[i]=="m":
            p+="z"
        elif palabra[i]=="n":
            p+="a"
        elif palabra[i]=="o":
            p+="b"
        elif palabra[i]=="p":
            p+="c"
        elif palabra[i]=="q":
            p+="d"
        elif palabra[i]=="r":
            p+="e"
        elif palabra[i]=="s":
            p+="f"
        elif palabra[i]=="t":
            p+="g"
        elif palabra[i]=="u":
            p+="h"
        elif palabra[i]=="v":
            p+="i"
        elif palabra[i]=="w":
            p+="j"
        elif palabra[i]=="x":
            p+="k"
        elif palabra[i]=="y":
            p+="l"
        elif palabra[i]=="z":
            p+="m"
    return p

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra=palabra.lower()
    print(rot13(palabra))
           