#Ordenar tres números
x = int(input("ingrese x"))
y = int(input("ingrese y"))
z = int(input("ingrese z"))

if x<y and x<z:
  if z<y:
    print(x,",",z,",",y)
  elif y<z:
    print(x,",",y,",",z)
elif y<z and y<x:
  if z<x:
    print(y,",",z,",",x)
  elif x<z:
    print(y,",",x,",",z)
elif z<x and z<y:
  if x<y:
    print(z,",",x,",",y)
  elif y<x:
    print(z,",",y,",",x)
if x==y and x==z:
  print(x,",",z,",",y)
elif x==y and x!=z:
  if x>z:
    print(z,",",x,",",y)
  elif x<z:
    print(x,",",y,",",z)
elif x==z and x!=y:
  if x>y:
    print(y,",",z,",",x)
  elif x<y:
    print(x,",",z,",",y)
elif z==y and z!=x:
  if z>x:
    print(x,",",z,",",y)
  elif z<x:
    print(y,",",z,",",x)