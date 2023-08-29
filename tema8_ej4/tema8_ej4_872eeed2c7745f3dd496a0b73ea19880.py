def rot13(palabra):

    r=""

    a=palabra

    for i in range(len(a)):

        if a[i]=="a":

            r=r+"n"

        elif a[i]=="b":

            r=r+"o"

        elif a[i]=="c":

            r=r+"p"

        elif a[i]=="d":

            r=r+"q"

        elif a[i]=="e":

            r=r+"r"

        elif a[i]=="f":

            r=r+"s"

        elif a[i]=="g":

            r=r+"t"

        elif a[i]=="h":

            r=r+"u"

        elif a[i]=="i":

            r=r+"v"

        elif a[i]=="j":

            r=r+"w"

        elif a[i]=="k":

            r=r+"x"

        elif a[i]=="l":

            r=r+"y"

        elif a[i]=="m":

            r=r+"z"

        elif a[i]=="n":

            r=r+"a"

        elif a[i]=="o":

            r=r+"b"

        elif a[i]=="p":

            r=r+"c"

        elif a[i]=="q":

            r=r+"d"

        elif a[i]=="r":

            r=r+"e"

        elif a[i]=="s":

            r=r+"f"

        elif a[i]=="t":

            r=r+"g"

        elif a[i]=="u":

            r=r+"h"

        elif a[i]=="v":

            r=r+"i"

        elif a[i]=="w":

            r=r+"j"

        elif a[i]=="x":

            r=r+"k"

        elif a[i]=="y":

            r=r+"l"

        elif a[i]=="z":

            r=r+"m"

        else:
            
            r=r+a[i]

    return r


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           