#Ordenar tres números
x=int(input("ingrese primer numero: ",))
y=int(input("ingrese segundo numero: ",))
z=int(input("ingrese tercer numero: ",))
if x<z<y:
  print (x,z,y)
elif y<z<y:
  print (y,z,y)
elif z<x<y:
  print (z,x,y)
elif z<y<x:
  print (z,y,x)