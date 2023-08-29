def rot13(palabra):
    s=list(palabra)
    for i in range(0,len(s)):
        if(s[i]<"n"):
            if(s[i]=="a"):
                s[i]="n"
            if(s[i]=="b"):
                s[i]="o"
            if(s[i]=="c"):
                s[i]="p"
            if(s[i]=="d"):
                s[i]="q"
            if(s[i]=="e"):
                s[i]="r"
            if(s[i]=="f"):
                s[i]="s"
            if(s[i]=="g"):
                s[i]="t"
            if(s[i]=="h"):
                s[i]="u"
            if(s[i]=="i"):
                s[i]="v"
            if(s[i]=="j"):
                s[i]="w"
            if(s[i]=="k"):
                s[i]="x"
            if(s[i]=="l"):
                s[i]="y"
            if(s[i]=="m"):
                s[i]="z"
        else:
            if(s[i]=="n"):
                s[i]="a"
            if(s[i]=="o"):
                s[i]="b"
            if(s[i]=="p"):
                s[i]="c"
            if(s[i]=="q"):
                s[i]="d"
            if(s[i]=="r"):
                s[i]="e"
            if(s[i]=="s"):
                s[i]="f"
            if(s[i]=="t"):
                s[i]="g"
            if(s[i]=="u"):
                s[i]="h"
            if(s[i]=="v"):
                s[i]="i"
            if(s[i]=="w"):
                s[i]="j"
            if(s[i]=="x"):
                s[i]="k"
            if(s[i]=="y"):
                s[i]="l"
            if(s[i]=="z"):
                s[i]="m"
    palabra="".join(s)
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)