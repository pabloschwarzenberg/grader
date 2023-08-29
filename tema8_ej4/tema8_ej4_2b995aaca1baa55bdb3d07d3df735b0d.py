def rot13(palabra):
    p1=list(palabra)
    for a in range(len(p1)):
      if p1[a]=="a":
        p1[a]="n"
      elif p1[a]=="b":
        p1[a]="o"
      elif p1[a]=="c":
        p1[a]="p"
      elif p1[a]=="d":
        p1[a]="q"
      elif p1[a]=="e":
        p1[a]="r"
      elif p1[a]=="f":
        p1[a]="s"
      elif p1[a]=="g":
        p1[a]="t"
      elif p1[a]=="h":
        p1[a]="u"
      elif p1[a]=="i":
        p1[a]="v"
      elif p1[a]=="j":
        p1[a]="w"
      elif p1[a]=="k":
        p1[a]="x"
      elif p1[a]=="l":
        p1[a]="y"
      elif p1[a]=="m":
        p1[a]="z"
      elif p1[a]=="n":
        p1[a]="a"
      elif p1[a]=="o":
        p1[a]="b"
      elif p1[a]=="p":
        p1[a]="c"
      elif p1[a]=="q":
        p1[a]="d"
      elif p1[a]=="r":
        p1[a]="e"
      elif p1[a]=="s":
        p1[a]="f"
      elif p1[a]=="t":
        p1[a]="g"
      elif p1[a]=="u":
        p1[a]="h"
      elif p1[a]=="v":
        p1[a]="i"
      elif p1[a]=="w":
        p1[a]="j"
      elif p1[a]=="x":
        p1[a]="k"
      elif p1[a]=="y":
        p1[a]="l"
      else:
        p1[a]="m"
    p1="".join(p1)
    return p1
pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           