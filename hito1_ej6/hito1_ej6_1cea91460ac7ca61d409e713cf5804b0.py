#Ordenar tres números
x=int(input())
y=int(input())
z=int(input())
if(x<=y<=z):
  print(x,",",y,",",z)
if(x<=z<=y):
  print(x,",",z,",",y)
if(y<=z<=x):
  print(y,",",z,",",x)
if(y<=x<=z):
  print(y,",",x,",",z)
if(z<=x<=y):
  print(z,",",x,",",y)
if(z<=y<=x):
  print(z,",",y,",",x)

 