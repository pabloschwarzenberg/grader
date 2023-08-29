#Ordenar tres númerosa 
a = int(input("Ingrese el 1er numero ->"))
b = int(input("Ingrese el 2do numero ->"))
c = int(input("Ingrese el 3er numero ->"))

if (a <= b):
  if (a <= c):
    if(b <= c):
      print(a,",",b,",",c)
    else:
      print(a,",",c,",",b)