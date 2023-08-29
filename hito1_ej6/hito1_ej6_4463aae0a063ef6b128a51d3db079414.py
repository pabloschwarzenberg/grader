#Ordenar tres números
a=int(input("ingrese el primer número"))
b=int(input("ingrese el segundo número"))
c=int(input("ingrese el tercer número"))
if(a<(min(b,c))):
  if(b<c):
    print(a,b,c,sep=", ")
  else:
    print(a,c,b,sep=", ")
else:
  if(b<(min(a,c))):
    if(a<c):
      print(b,a,c,sep=", ")
    else:
      print(b,c,a,sep=", ")
  else:
    if(a<b):
      print(c,a,b,sep=", ")
    else:
      print(c,b,a,sep=", ")