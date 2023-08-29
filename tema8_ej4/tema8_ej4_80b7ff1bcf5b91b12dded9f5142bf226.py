def rot13(palabra):
    L=list(palabra)
    i=0
    while i < len(L):
        if L[i]=="a":
            L[i]="n"
            i=i+1
        elif L[i]=="b":
            L[i]="o"
            i=i+1
        elif L[i]=="c":
            L[i]="p"
            i=i+1
        elif L[i]=="d":
            L[i]="q"
            i=i+1
        elif L[i]=="e":
            L[i]="r"
            i=i+1
        elif L[i]=="f":
            L[i]="s"
            i=i+1
        elif L[i]=="g":
            L[i]="t"
            i=i+1
        elif L[i]=="h":
            L[i]="u"
            i=i+1
        elif L[i]=="i":
            L[i]="v"
            i=i+1
        elif L[i]=="j":
            L[i]="w"
            i=i+1
        elif L[i]=="k":
            L[i]="x"
            i=i+1
        elif L[i]=="l":
            L[i]="y"
            i=i+1
        elif L[i]=="m":
            L[i]="z"
            i=i+1
        elif L[i]=="n":
            L[i]="a"
            i=i+1
        elif L[i]=="o":
            L[i]="b"
            i=i+1
        elif L[i]=="p":
            L[i]="c"
            i=i+1
        elif L[i]=="q":
            L[i]="d"
            i=i+1
        elif L[i]=="r":
            L[i]="e"
            i=i+1
        elif L[i]=="s":
            L[i]="f"
            i=i+1
        elif L[i]=="t":
            L[i]="g"
            i=i+1
        elif L[i]=="u":
            L[i]="h"
            i=i+1
        elif L[i]=="v":
            L[i]="i"
            i=i+1
        elif L[i]=="w":
            L[i]="j"
            i=i+1
        elif L[i]=="x":
            L[i]="k"
            i=i+1
        elif L[i]=="y":
            L[i]="l"
            i=i+1
        elif L[i]=="z":
            L[i]="m"
            i=i+1
    palabra="".join(L)
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)