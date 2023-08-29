def rot13(palabra):
  a=list(palabra)
  i=0
  while i<len(a):
    if a[i]=="a":
      a[i]="n"
    elif a[i]=="b":
      a[i]="o"
    elif a[i]=="c":
      a[i]="p"
    elif a[i]=="d":
      a[i]="q"
    elif a[i]=="e":
      a[i]="r"
    elif a[i]=="f":
      a[i]="s"
    elif a[i]=="g":
      a[i]="t"
    elif a[i]=="h":
      a[i]="u"
    elif a[i]=="i":
      a[i]="v"
    elif a[i]=="j":
      a[i]="w"
    elif a[i]=="k":
      a[i]="x"
    elif a[i]=="l":
      a[i]="y"
    elif a[i]=="m":
      a[i]="z"
    elif a[i]=="n":
      a[i]="a"
    elif a[i]=="o":
      a[i]="b"
    elif a[i]=="p":
      a[i]="c"
    elif a[i]=="q":
      a[i]="d"
    elif a[i]=="r":
      a[i]="e"
    elif a[i]=="s":
      a[i]="f"
    elif a[i]=="t":
      a[i]="g"
    elif a[i]=="u":
      a[i]="h"
    elif a[i]=="v":
      a[i]="i"
    elif a[i]=="w":
      a[i]="j"
    elif a[i]=="x":
      a[i]="k"
    elif a[i]=="y":
      a[i]="l"
    elif a[i]=="z":
      a[i]="m"
    i=i+1
  b="".join(a)
  return b
           