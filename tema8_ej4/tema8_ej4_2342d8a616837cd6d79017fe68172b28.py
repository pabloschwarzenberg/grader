def rot13(palabra):
    palabra_l=list(palabra)
    rot13=""
    rot13_l=list(rot13)
    for n in palabra_l:
        if n=="a":
            n="n"
        elif n=="b":
            n="o"
        elif n=="c":
            n="p"
        elif n=="d":
            n="q"
        elif n=="e":
            n="r"
        elif n=="f":
            n="s"
        elif n=="g":
            n="t"
        elif n=="h":
            n="u"
        elif n=="i":
            n="v"
        elif n=="j":
            n="w"
        elif n=="k":
            n="x"
        elif n=="l":
            n="y"
        elif n=="m":
            n="z"
        elif n=="n":
            n="a"
        elif n=="o":
            n="b"
        elif n=="p":
            n="c"
        elif n=="q":
            n="d"
        elif n=="r":
            n="e"
        elif n=="s":
            n="f"
        elif n=="t":
            n="g"
        elif n=="u":
            n="h"
        elif n=="v":
            n="i"
        elif n=="w":
            n="j"
        elif n=="x":
            n="k"
        elif n=="y":
            n="l"
        elif n=="z":
            n="m"
        rot13_l.append(n)
        rot13="".join(rot13_l)
    return rot13
print(rot13)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           
          