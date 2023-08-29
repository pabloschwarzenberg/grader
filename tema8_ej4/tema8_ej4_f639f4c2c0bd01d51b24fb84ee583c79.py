def rot13(palabra):
    pal=[]
    for i in palabra:
      if i=="a":
        pal.append("n")
      if i=="b":
        pal.append("o")
      if i=="c":
        pal.append("p")
      if i=="d":
        pal.append("q")
      if i=="e":
        pal.append("r")
      if i=="f":
        pal.append("s")
      if i=="g":
        pal.append("t")
      if i=="h":
        pal.append("u")
      if i=="i":
        pal.append("v")
      if i=="j":
        pal.append("w")
      if i=="k":
        pal.append("x")
      if i=="l":
        pal.append("y")
      if i=="m":
        pal.append("z")
      if i=="n":
        pal.append("a")
      if i=="o":
        pal.append("b")
      if i=="p":
        pal.append("c")
      if i=="q":
        pal.append("d")
      if i=="r":
        pal.append("e")
      if i=="s":
        pal.append("f")
      if i=="t":
        pal.append("g")
      if i=="u":
        pal.append("h")
      if i=="v":
        pal.append("i")
      if i=="w":
        pal.append("j")
      if i=="x":
        pal.append("k")
      if i=="y":
        pal.append("l")
      if i=="z":
        pal.append("m")
    word="".join(pal)
    return word
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           