def rot13(palabra):
    lista_palabra=list(palabra)
    largo_palabra=len(palabra)
    i=0
    while i<largo_palabra:
        if palabra[i]=="a":
            lista_palabra[i]="n"
        elif palabra[i]=="b":
            lista_palabra[i] ="o"
        elif palabra[i]=="c":
            lista_palabra[i] ="p"
        elif palabra[i]=="d":
            lista_palabra[i] ="q"
        elif palabra[i]=="e":
            lista_palabra[i] ="r"
        elif palabra[i]=="f":
            lista_palabra[i] ="s"
        elif palabra[i]=="g":
            lista_palabra[i] ="t"
        elif palabra[i]=="h":
            lista_palabra[i] ="u"
        elif palabra[i]=="i":
            lista_palabra[i] ="v"
        elif palabra[i]=="j":
            lista_palabra[i] ="w"
        elif palabra[i]=="k":
            lista_palabra[i] ="x"
        elif palabra[i]=="l":
            lista_palabra[i] ="y"
        elif palabra[i]=="m":
            lista_palabra[i] ="z"
        elif palabra[i]=="n":
            lista_palabra[i] ="a"
        elif palabra[i]=="o":
            lista_palabra[i] ="b"
        elif palabra[i]=="p":
            lista_palabra[i] ="c"
        elif palabra[i]=="q":
            lista_palabra[i] ="d"
        elif palabra[i]=="r":
            lista_palabra[i] ="e"
        elif palabra[i]=="s":
            lista_palabra[i] ="f"
        elif palabra[i]=="t":
            lista_palabra[i] ="g"
        elif palabra[i]=="u":
            lista_palabra[i] ="h"
        elif palabra[i]=="v":
            lista_palabra[i] ="i"
        elif palabra[i]=="w":
            lista_palabra[i] ="j"
        elif palabra[i]=="x":
            lista_palabra[i] ="k"
        elif palabra[i]=="y":
            lista_palabra[i] ="l"
        elif palabra[i]=="z":
            lista_palabra[i] ="m"
        i=i+1
    return "".join(lista_palabra)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           