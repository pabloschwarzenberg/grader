def rot13(palabra):
    i=0
    palabra1=list(palabra)
    while i<len(palabra):
        if palabra1[i]=="a":
            palabra1[i]="n"
        elif palabra1[i]=="b":
            palabra1[i]="o"
        elif palabra1[i]=="c":
            palabra1[i]="p"
        elif palabra1[i]=="d":
            palabra1[i]="q"
        elif palabra1[i]=="e":
            palabra1[i]="r"
        elif palabra1[i]=="f":
            palabra1[i]="s"
        elif palabra1[i]=="g":
            palabra1[i]="t"
        elif palabra1[i]=="h":
            palabra1[i]="u"
        elif palabra1[i]=="i":
            palabra1[i]="v"
        elif palabra1[i]=="j":
            palabra1[i]="w"
        elif palabra1[i]=="k":
            palabra1[i]="x"
        elif palabra1[i]=="l":
            palabra1[i]="y"
        elif palabra1[i]=="m":
            palabra1[i]="z"
        elif palabra1[i]=="n":
            palabra1[i]="a"
        elif palabra1[i]=="o":
            palabra1[i]="b"
        elif palabra1[i]=="p":
            palabra1[i]="c"
        elif palabra1[i]=="q":
            palabra1[i]="d"
        elif palabra1[i]=="r":
            palabra1[i]="e"
        elif palabra1[i]=="s":
            palabra1[i]="f"
        elif palabra1[i]=="t":
            palabra1[i]="g"
        elif palabra1[i]=="u":
            palabra1[i]="h"
        elif palabra1[i]=="v":
            palabra1[i]="i"
        elif palabra1[i]=="w":
            palabra1[i]="j"
        elif palabra1[i]=="x":
            palabra1[i]="k"
        elif palabra1[i]=="y":
            palabra1[i]="l"
        elif palabra1[i]=="z":
            palabra1[i]="m"
        i+=1
        palabra="".join(palabra1)
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           