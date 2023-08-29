def rot13(palabra):
    a=list(palabra)
    for i in range (0,len(a)):
        if(a[i]<"n"):
            if(a[i]=="a"):
                a[i]="n"
            if(a[i]=="b"):
                a[i]="o"
            if(a[i]=="c"):
                a[i]="p"
            if(a[i]=="d"):
                a[i]="q"
            if(a[i]=="e"):
               a[i]="r"
            if(a[i]=="f"):
               a[i]="s"
            if(a[i]=="g"):
                a[i]="t"
            if(a[i]=="h"):
                a[i]="u"
            if(a[i]=="i"):
                a[i]="v"
            if(a[i]=="j"):
                a[i]="w"
            if(a[i]=="k"):
                a[i]="x"
            if(a[i]=="l"):
                a[i]="y"
            if(a[i]=="m"):
                a[i]="z"
        else:
            if(a[i]=="n"):
                a[i]="a"
            if(a[i]=="o"):
                a[i]="b"
            if(a[i]=="p"):
                a[i]="c"
            if(a[i]=="q"):
                a[i]="c"
            if(a[i]=="r"):
               a[i]="e"
            if(a[i]=="s"):
               a[i]="f"
            if(a[i]=="t"):
                a[i]="g"
            if(a[i]=="u"):
                a[i]="h"
            if(a[i]=="v"):
                a[i]="i"
            if(a[i]=="w"):
                a[i]="j"
            if(a[i]=="x"):
                a[i]="k"
            if(a[i]=="y"):
                a[i]="l"
            if(a[i]=="z"):
                a[i]="m"
    palabra="".join(a)
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           