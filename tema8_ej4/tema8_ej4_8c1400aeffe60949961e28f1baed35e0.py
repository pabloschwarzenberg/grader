def rot13(palabra):
    palabra_cifrada=""
    for j in range(0,len(palabra)):
        if palabra[j]=="a":
            palabra_cifrada += "n"
        if palabra[j]=="b":
            palabra_cifrada += "o"
        if palabra[j]=="c":
            palabra_cifrada += "p"
        if palabra[j]=="d":
            palabra_cifrada +="q"
        if palabra[j]=="e":
            palabra_cifrada += "r"
        if palabra[j]=="f":
            palabra_cifrada += "s"
        if palabra[j]=="g":
            palabra_cifrada += "t"
        if palabra[j]=="h":
            palabra_cifrada +="u"
        if palabra[j]=="i":
            palabra_cifrada += "v"
        if palabra[j]=="j":
            palabra_cifrada += "w"
        if palabra[j]=="k":
            palabra_cifrada += "x"
        if palabra[j]=="l":
            palabra_cifrada +="y"
        if palabra[j]=="m":
            palabra_cifrada += "z"
        if palabra[j]=="n":
            palabra_cifrada += "a"
        if palabra[j]=="o":
            palabra_cifrada += "b"
        if palabra[j]=="p":
            palabra_cifrada +="c"
        if palabra[j]=="q":
            palabra_cifrada +="d"
        if palabra[j]=="r":
            palabra_cifrada += "e"
        if palabra[j]=="s":
            palabra_cifrada += "f"
        if palabra[j]=="t":
            palabra_cifrada += "g"
        if palabra[j]=="u":
            palabra_cifrada +="h"
        if palabra[j]=="v":
            palabra_cifrada += "i"
        if palabra[j]=="w":
            palabra_cifrada += "j"
        if palabra[j]=="x":
            palabra_cifrada += "k"
        if palabra[j]=="y":
            palabra_cifrada +="l"
        if palabra[j]=="z":
            palabra_cifrada +="m"

            
    return palabra_cifrada

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           