import string
def rot13(palabra1):
    i=int(0)
    n=int(len(palabra1))
    palabra=list(palabra1)
    while i<n:
          if palabra[i]=="a":
             palabra[i]="n"
          elif palabra[i]=="b":
             palabra[i]="o"
          elif palabra[i]=="c":
             palabra[i]="p"
          elif palabra[i]=="d":
             palabra[i]="q"
          elif palabra[i]=="e":
             palabra[i]="r"
          elif palabra[i]=="f":
             palabra[i]="s"
          elif palabra[i]=="g":
             palabra[i]="t"
          elif palabra[i]=="h":
             palabra[i]="u"
          elif palabra[i]=="i":
             palabra[i]="v"
          elif palabra[i]=="j":
             palabra[i]="w"
          elif palabra[i]=="k":
             palabra[i]="x"
          elif palabra[i]=="l":
             palabra[i]="y"
          elif palabra[i]=="m":
             palabra[i]="z"
          elif palabra[i]=="n":
             palabra[i]="a"
          elif palabra[i]=="o":
             palabra[i]="b"
          elif palabra[i]=="p":
             palabra[i]="c"
          elif palabra[i]=="q":
             palabra[i]="d"
          elif palabra[i]=="r":
             palabra[i]="e"
          elif palabra[i]=="s":
             palabra[i]="f"
          elif palabra[i]=="t":
             palabra[i]="g"
          elif palabra[i]=="u":
             palabra[i]="h"
          elif palabra[i]=="v":
             palabra[i]="i"
          elif palabra[i]=="w":
             palabra[i]="j"
          elif palabra[i]=="x":
             palabra[i]="k"
          elif palabra[i]=="y":
             palabra[i]="l"
          elif palabra[i]=="z":
             palabra[i]="m"
          i+=1
    palabra2="".join(palabra)
    return palabra2