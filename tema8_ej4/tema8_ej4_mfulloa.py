def rot13(palabra):
    r=list(palabra)
    for i in range(len(r)):
        if r[i]=="a":
            r[i]="n"
        elif r[i]=="b":
            r[i]="o"
        elif r[i]=="c":
            r[i]="p"
        elif r[i]=="d":
            r[i]="q"
        elif r[i]=="e":
            r[i]="r"
        elif r[i]=="f":
            r[i]="s"
        elif r[i]=="g":
            r[i]="t"
        elif r[i]=="h":
            r[i]="u"
        elif r[i]=="i":
            r[i]="v"
        elif r[i]=="j":
            r[i]="w"
        elif r[i]=="k":
            r[i]="x"
        elif r[i]=="l":
            r[i]="y"
        elif r[i]=="m":
            r[i]="z"
        elif r[i]=="n":
            r[i]="a"
        elif r[i]=="o":
            r[i]="b"
        elif r[i]=="p":
            r[i]="c"
        elif r[i]=="q":
            r[i]="d"
        elif r[i]=="r":
            r[i]="e"
        elif r[i]=="s":
            r[i]="f"
        elif r[i]=="t":
            r[i]="g"
        elif r[i]=="u":
            r[i]="h"
        elif r[i]=="v":
            r[i]="i"
        elif r[i]=="w":
            r[i]="j"
        elif r[i]=="x":
            r[i]="k"
        elif r[i]=="y":
            r[i]="l"
        elif r[i]=="z":
            r[i]="m"
    return "".join(r)
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           