def rot13(palabra):
    t=""
    for i in palabra:
      if i=="a":
        t=t+"n"
      if i=="b":
        t=t+"o"
      if i=="c":
        t=t+"p"
      if i=="d":
        t=t+"q"
      if i=="e":
        t=t+"r"
      if i=="f":
        t=t+"s"
      if i=="g":
        t=t+"t"
      if i=="h":
        t=t+"u"
      if i=="i":
        t=t+"v"
      if i=="j":
        t=t+"w"
      if i=="k":
        t=t+"x"
      if i=="l":
        t=t+"y"
      if i=="m":
        t=t+"z"
      if i=="n":
        t=t+"a"
      if i=="o":
        t=t+"b"
      if i=="p":
        t=t+"c"
      if i=="q":
        t=t+"d"
      if i=="r":
        t=t+"e"
      if i=="s":
        t=t+"f"
      if i=="t":
        t=t+"g"
      if i=="u":
        t=t+"h"
      if i=="v":
        t=t+"i"
      if i=="w":
        t=t+"j"
      if i=="x":
        t=t+"k"
      if i=="y":
        t=t+"l"
      if i=="z":
        t=t+"m"
    return(t)    
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           