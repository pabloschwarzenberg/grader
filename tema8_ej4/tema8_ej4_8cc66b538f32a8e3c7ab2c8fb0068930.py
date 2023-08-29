def rot13(palabra):
    list_resultado=[]
    for ñ in palabra:
        if ñ=="a":
            list_resultado.append("n")
        if ñ=="b":
            list_resultado.append("o")
        if ñ=="c":
            list_resultado.append("p")
        if ñ=="d":
            list_resultado.append("q")
        if ñ=="e":
            list_resultado.append("r")
        if ñ=="f":
            list_resultado.append("s")
        if ñ=="g":
            list_resultado.append("t")
        if ñ=="h":
            list_resultado.append("u")
        if ñ=="i":
            list_resultado.append("v")
        if ñ=="j":
            list_resultado.append("w")
        if ñ=="k":
            list_resultado.append("x")
        if ñ=="l":
            list_resultado.append("y")
        if ñ=="m":
            list_resultado.append("z")
        if ñ=="n":
            list_resultado.append("a")
        if ñ=="o":
            list_resultado.append("b")
        if ñ=="p":
            list_resultado.append("c")
        if ñ=="q":
            list_resultado.append("d")
        if ñ=="r":
            list_resultado.append("e")
        if ñ=="s":
            list_resultado.append("f")
        if ñ=="t":
            list_resultado.append("g")
        if ñ=="u":
            list_resultado.append("h")
        if ñ=="v":
            list_resultado.append("i")
        if ñ=="w":
            list_resultado.append("j")
        if ñ=="x":
            list_resultado.append("k")
        if ñ=="y":
            list_resultado.append("l")
        if ñ=="z":
            list_resultado.append("m")
    resultado="".join(list_resultado)
    return resultado
    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)