def rot13(palabra):
    palabra_l=list(palabra)
    for i in range(0,len(palabra)):
        if palabra_l[i]=="a":
            palabra_l[i]="n"
        elif palabra_l[i]=="b":
            palabra_l[i]="o"
        elif palabra_l[i]=="c":
            palabra_l[i]="p"
        elif palabra_l[i]=="d":
            palabra_l[i]="q"
        elif palabra_l[i]=="e":
            palabra_l[i]="r"
        elif palabra_l[i]=="f":
            palabra_l[i]="s"
        elif palabra_l[i]=="g":
            palabra_l[i]="t"
        elif palabra_l[i]=="h":
            palabra_l[i]="u"
        elif palabra_l[i]=="i":
            palabra_l[i]="v"
        elif palabra_l[i]=="j":
            palabra_l[i]="w"
        elif palabra_l[i]=="k":
            palabra_l[i]="x"
        elif palabra_l[i]=="l":
            palabra_l[i]="y"
        elif palabra_l[i]=="m":
            palabra_l[i]="z"
        elif palabra_l[i]=="n":
            palabra_l[i]="a"
        elif palabra_l[i]=="o":
            palabra_l[i]="b"
        elif palabra_l[i]=="p":
            palabra_l[i]="c"
        elif palabra_l[i]=="q":
            palabra_l[i]="d"
        elif palabra_l[i]=="r":
            palabra_l[i]="e"
        elif palabra_l[i]=="s":
            palabra_l[i]="f"
        elif palabra_l[i]=="t":
            palabra_l[i]="g"
        elif palabra_l[i]=="u":
            palabra_l[i]="h"
        elif palabra_l[i]=="v":
            palabra_l[i]="i"
        elif palabra_l[i]=="w":
            palabra_l[i]="j"
        elif palabra_l[i]=="x":
            palabra_l[i]="k"
        elif palabra_l[i]=="y":
            palabra_l[i]="l"
        elif palabra_l[i]=="z":
            palabra_l[i]="m"
    palabra="".join(palabra_l)
        
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           