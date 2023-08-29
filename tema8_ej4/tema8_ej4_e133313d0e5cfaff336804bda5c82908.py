def rot13(palabra):
    letras=list(palabra)
    for i in range(len(letras)):
        if letras[i]=="a":
            letras[i]="n"
        else:
            if letras[i]=="b":
                letras[i]="o"
            else:
                if letras[i]=="c":
                    letras[i]="p"
                else:
                    if letras[i]=="d":
                        letras[i]="q"
                    else:
                        if letras[i]=="e":
                            letras[i]="r"
                        else:
                            if letras[i]=="f":
                                letras[i]="s"
                            else:
                                if letras[i]=="g":
                                    letras[i]="t"
                                else:
                                    if letras[i]=="h":
                                        letras[i]="u"
                                    else:
                                        if letras[i]=="i":
                                            letras[i]="v"
                                        else:
                                            if letras[i]=="j":
                                                letras[i]="w"
                                            else:
                                                if letras[i]=="k":
                                                    letras[i]="x"
                                                else:
                                                    if letras[i]=="l":
                                                        letras[i]="y"
                                                    else:
                                                        if letras[i]=="m":
                                                            letras[i]="z"
                                                        else:
                                                            if letras[i]=="n":
                                                                letras[i]="a"
                                                            else:
                                                                if letras[i]=="o":
                                                                    letras[i]="b"
                                                                else:
                                                                    if letras[i]=="p":
                                                                        letras[i]="c"    
                                                                    else:
                                                                        if letras[i]=="q":
                                                                            letras[i]="d"
                                                                        else:
                                                                            if letras[i]=="r":
                                                                                 letras[i]="e"
                                                                            else:
                                                                                if letras[i]=="s":
                                                                                    letras[i]="f"
                                                                                else:
                                                                                    if letras[i]=="t":
                                                                                        letras[i]="g"
                                                                                    else:              
                                                                                        if letras[i]=="u":
                                                                                            letras[i]="h"
                                                                                        else:
                                                                                            if letras[i]=="v":
                                                                                                letras[i]="i"
                                                                                            else:
                                                                                                if letras[i]=="w":
                                                                                                    letras[i]="j"
                                                                                                else:
                                                                                                    if letras[i]=="x":
                                                                                                        letras[i]="k"
                                                                                                    else:
                                                                                                        if letras[i]=="y":
                                                                                                            letras[i]="l"
                                                                                                        else:
                                                                                                            if letras[i]=="z":
                                                                                                                letras[i]="m"
    palabra="".join(letras)
    return palabra
   
                                                                                   
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           