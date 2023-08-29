#Ordenar tres números
x = int(input("ingrese numero: "))
y = int(input("ingrese numero: "))
z = int(input("ingrese numero: "))

if x<=y<=z:
  print(x,",",y,",",z)
elif x<=z<=y:
  print(x,",",z,",",y)
elif y<=x<=z:
  print(y,",",x,",",z)
elif y<=z<=x:
  print(y,",",z,",",x)
elif z<=x<=y:
  print(z,",",x,",",y)
else:
  print(z,",",y,",",x)