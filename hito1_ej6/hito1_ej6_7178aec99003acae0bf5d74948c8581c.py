#Ordenar tres números
x=int(input())
y=int(input())
z=int(input())
if x<y and y<z:
  print(x,"," , y,",", z)
if x==z and y==z:
  print(x, ",", y, ",", z)
if x<=z and z<y:
  print(x,",", z,",", y)
if z<=y and y<x:
  print(z,",", y,",", x)
if z<=x and x<y:
  print(z,",", x,",", y)
if y<=x and x<z:
  print(y,",", x,",", z)
if y<=z and z<x:
  print(y,",", z,",", x)
if x<z and z<=y:
  print(x,",", z,",", y)
if z<y and x<=y:
  print(z,",", y,",", x)
if z<x and x<=y:
  print(z,",", x,",", y)
if y<x and x<=z:
  print(y,",", x,",", z)
if y<z and z<=x:
  print(y,",", z,",", x)

