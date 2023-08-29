def rot13(palabra):
    i=0
    x=""
    while i<len(palabra):   
        if palabra[i]=="a":
            x=x+"n"
            i=i+1

        elif palabra[i]=="b":
            x=x+"o"
            i=i+1

        elif palabra[i]=="c":
            x=x="p"
            i=i+1

        elif palabra[i]=="d":
            x=x+"q"
            i=i+1

        elif palabra[i]=="e":
            x=x+"r"
            i=i+1

        elif palabra[i]=="f":
            x=x+"s"
            i=i+1

        elif palabra[i]=="g":
            x=x+"t"
            i=i+1

        elif palabra[i]=="h":
            x=x+"u"
            i=i+1

        elif palabra[i]=="i":
            x=x+"v"
            i=i+1

        elif palabra[i]=="j":
            x=x+"w"
            i=i+1

        elif palabra[i]=="k":
            x=x+"x"
            i=i+1

        elif palabra[i]=="l":
            x=x+"y"
            i=i+1

        elif palabra[i]=="m":
            x=x+"z"
            i=i+1

        elif palabra[i]=="n":
            x=x+"a"
            i=i+1

        elif palabra[i]=="o":
            x=x+"b"
            i=i+1

        elif palabra[i]=="p":
            x=x+"c"
            i=i+1

        elif palabra[i]=="q":
            x=x+"d"
            i=i+1

        elif palabra[i]=="r":
            x=x+"e"
            i=i+1

        elif palabra[i]=="s":
            x=x+"f"
            i=i+1

        elif palabra[i]=="t":
            x=x+"g"
            i=i+1

        elif palabra[i]=="u":
            x=x+"h"
            i=i+1

        elif palabra[i]=="v":
            x=x+"i"
            i=i+1

        elif palabra[i]=="w":
            x=x+"j"
            i=i+1

        elif palabra[i]=="x":
            x=x+"k"
            i=i+1

        elif palabra[i]=="y":
            x=x+"l"
            i=i+1

        elif palabra[i]=="z":
            x=x+"m"
            i=i+1
    return x