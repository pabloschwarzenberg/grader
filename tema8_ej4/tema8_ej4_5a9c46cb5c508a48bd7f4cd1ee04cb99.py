def rot13(palabra):
  lista=list(palabra)
  i=0
  while i<len(lista):
    if lista[i]=="a":
      lista[i]="n"
    elif lista[i]=="b":
      lista[i]="o"
    elif lista[i]=="c":
      lista[i]="p"
    elif lista[i]=="d":
      lista[i]="q"
    elif lista[i]=="e":
      lista[i]="r"
    elif lista[i]=="f":
      lista[i]="s"
    elif lista[i]=="g":
      lista[i]="t"
    elif lista[i]=="h":
      lista[i]="u"
    elif lista[i]=="i":
      lista[i]="v"
    elif lista[i]=="j":
      lista[i]="w"
    elif lista[i]=="k":
      lista[i]="x"
    elif lista[i]=="l":
      lista[i]="y"
    elif lista[i]=="m":
      lista[i]="z"
    elif lista[i]=="n":
      lista[i]="a"
    elif lista[i]=="o":
      lista[i]="b"
    elif lista[i]=="p":
      lista[i]="c"
    elif lista[i]=="q":
      lista[i]="d"
    elif lista[i]=="r":
      lista[i]="e"
    elif lista[i]=="s":
      lista[i]="f"
    elif lista[i]=="t":
      lista[i]="g"
    elif lista[i]=="u":
      lista[i]="h"
    elif lista[i]=="v":
      lista[i]="i"
    elif lista[i]=="w":
      lista[i]="j"
    elif lista[i]=="x":
      lista[i]="k"
    elif lista[i]=="y":
      lista[i]="l"
    elif lista[i]=="z":
      lista[i]="m"
    i=i+1
    a="".join(lista)
  return a