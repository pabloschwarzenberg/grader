def rot13(palabra):
    lista = []
    for letra in palabra:
        lista.append(letra)
    x = len(lista)
    for i in range(x):
            if lista[i]=="a":
                lista.append("n")
            if lista[i]=="b":
                lista.append("o")
            if lista[i]=="c":
                lista.append("p")
            if lista[i]=="d":
                lista.append("q")
            if lista[i]=="e":
                lista.append("r")
            if lista[i]=="f":
                lista.append("s")
            if lista[i]=="g":
                lista.append("t")
            if lista[i]=="h":
                lista.append("u")
            if lista[i]=="i":
                lista.append("v")
            if lista[i]=="j":
                lista.append("w")
            if lista[i]=="k":
                lista.append("x")
            if lista[i]=="l":
                lista.append("y")
            if lista[i]=="m":
                lista.append("z")
            if lista[i]=="n":
                lista.append("a")
            if lista[i]=="o":
                lista.append("b")
            if lista[i]=="p":
                lista.append("c")
            if lista[i]=="q":
                lista.append("d")
            if lista[i]=="r":
                lista.append("e")
            if lista[i]=="s":
                lista.append("f")
            if lista[i]=="t":
                lista.append("g")
            if lista[i]=="u":
                lista.append("h")
            if lista[i]=="v":
                lista.append("i")
            if lista[i]=="w":
                lista.append("j")
            if lista[i]=="x":
                lista.append("k")
            if lista[i]=="y":
                lista.append("l")
            if lista[i]=="z":
                lista.append("m")

    j = 0
    while j<(len(lista)-x):
             lista.remove(lista[j])
    j = j + 1
    cadena = "".join(lista)
    return cadena
            

    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           