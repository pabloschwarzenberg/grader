x=int(input("ingrese x: "))
y=int(input("ingrese y: "))
z=int(input("ingrese z: "))


if x<y<z:
  print(x,",",y,",",z)
if x<z<y:
  print(x,",",z,",",y)
if y<x<z:
  print(y,",",x,",",z)  
if y<z<x:
  print(y,",",z,",",x)
if z<x<y:
  print(z,",",x,",",y)
if z<y<x:
  print(z,",",y,",",x)
if x==y<z:
  print(x,",",y,",",z)  
if x==z<y:
  print(x,",",z,",",y)  
if z==y<x:
  print(z,",",y,",",x)
