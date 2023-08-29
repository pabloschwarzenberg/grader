def rot13(palabra):
    s=""
    for i in palabra:
        if i=="a":
            s = s+"n"
        elif i=="b":
            s = s+"o"
        elif i=="c":
            s = s+"p"
        elif i=="d":
            s = s+"q"
        elif i=="e":
            s = s+"r"
        elif i=="f":
            s = s+"s"
        elif i=="g":
            s = s+"t"
        elif i=="h":
            s = s+"u"
        elif i=="i":
            s = s+"v"
        elif i=="j":
            s = s+"w"
        elif i=="k":
            s = s+"x"
        elif i=="l":
            s = s+"y"
        elif i=="m":
            s = s+"z"
        elif i=="n":
            s = s+"a"
        elif i=="o":
            s = s+"b"
        elif i=="p":
            s = s+"c"
        elif i=="q":
            s = s+"d"
        elif i=="r":
            s = s+"e"
        elif i=="s":
            s = s+"f"
        elif i=="t":
            s = s+"g"
        elif i=="u":
            s = s+"h"
        elif i=="v":
            s = s+"i"
        elif i=="w":
            s = s+"j"
        elif i=="x":
            s = s+"k"
        elif i=="y":
            s = s+"l"
        elif i=="z":
            s = s+"m"
    return s
            

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           