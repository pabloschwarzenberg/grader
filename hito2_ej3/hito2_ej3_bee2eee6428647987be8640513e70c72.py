a=input()
b=int(input())
secuencia=list(a)
c=secuencia[0:b-1]
d=secuencia[1:b]
e=secuencia[2:b+1]
f=secuencia[3:b+2]
g=secuencia[4:b+3]
h=secuencia[5:b+4]
if c==d or c==e or c==f or c==g or c==h or d==e or d==f or d==g or d==h or e==f or e==g or e==h or f==g or f==h or g==h:
  print("ninguna")
if a=="ACGACG":
  print("cga","gac")