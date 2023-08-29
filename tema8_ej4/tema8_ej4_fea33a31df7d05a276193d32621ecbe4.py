def rot13(palabra):
    palabra=list(palabra)
    h=[]
    for i in range(len(palabra)):
      if palabra[i]=="a":
          palabra[i]="n"
          h.append(palabra[i])
      elif palabra[i]=="b":
          palabra[i]="o"
          h.append(palabra[i])
      elif palabra[i]=="c":
          palabra[i]="p"
          h.append(palabra[i])
      elif palabra[i]=="d":
          palabra[i]="q"
          h.append(palabra[i])
      elif palabra[i]=="e":
          palabra[i]="r"
          h.append(palabra[i])
      elif palabra[i]=="f":
          palabra[i]="s"
          h.append(palabra[i])
      elif palabra[i]=="g":
          palabra[i]="t"
          h.append(palabra[i])
      elif palabra[i]=="h":
          palabra[i]="u"
          h.append(palabra[i])
      elif palabra[i]=="i":
          palabra[i]="v"
          h.append(palabra[i])
      elif palabra[i]=="j":
          palabra[i]="w"
          h.append(palabra[i])
      elif palabra[i]=="k":
          palabra[i]="x"
          h.append(palabra[i])
      elif palabra[i]=="l":
          palabra[i]="y"
          h.append(palabra[i])
      elif palabra[i]=="m":
          palabra[i]="z"
          h.append(palabra[i])
      elif palabra[i]=="n":
          palabra[i]="a"
          h.append(palabra[i])
      elif palabra[i]=="o":
          palabra[i]="b"
          h.append(palabra[i])
      elif palabra[i]=="p":
          palabra[i]="c"
          h.append(palabra[i])
      elif palabra[i]=="q":
          palabra[i]="d"
          h.append(palabra[i])
      elif palabra[i]=="r":
          palabra[i]="e"
          h.append(palabra[i])
      elif palabra[i]=="s":
          palabra[i]="f"
          h.append(palabra[i])
      elif palabra[i]=="t":
          palabra[i]="g"
          h.append(palabra[i])
      elif palabra[i]=="u":
          palabra[i]="h"
          h.append(palabra[i])
      elif palabra[i]=="v":
          palabra[i]="i"
          h.append(palabra[i])
      elif palabra[i]=="w":
          palabra[i]="j"
          h.append(palabra[i])
      elif palabra[i]=="x":
          palabra[i]="k"
          h.append(palabra[i])
      elif palabra[i]=="y":
          palabra[i]="l"
          h.append(palabra[i])
      elif palabra[i]=="z":
          palabra[i]="m"
          h.append(palabra[i])
    h="".join(h)
    return h


if __name__=="__main__":
   palabra=input("Ingresa la palabra que quieras encriptar: ")
   palabra=palabra.lower()
   print(palabra)
   palabra=list(palabra)
   resultado=rot13(palabra)
   resultado="".join(resultado)
   print("El resultado es: ",resultado)
           
           