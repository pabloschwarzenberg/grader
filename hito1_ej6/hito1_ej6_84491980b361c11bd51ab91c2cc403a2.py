#Ordenar tres números#Rodrigo Martinez
x=int(input("ingrese un numero"))
y=int(input("ingrese un numero distinto de x"))
z=int(input("ingrese un numero distinto de x,y"))
if(x<y and y<z):
  print(x,",",y,",",z)
if(y<x and x<z):
  print(y,",",x,",",z)
if(z<x and x<y):
  print(z,",",x,",",y)
if(z<y and y<x):
  print(z,",",y,",",x)
if(x<z and z<y):
  print(x,",",z,",",y)
if(y<z and z<x):
  print(y,",",z,",",x)
if(x==y and y<z):
  print(x,",",y,",",z)
if(z==y and y<x):
  print(z,",",y,",",x)
if(x<z and z==y):
  print(x,",",z,",",y)
if(z<x and z==y):
  print(z,",",y,",",x)
if(z==x and z==y):
  print(z,",",x,",",y)
if(y<z and z==x):
  print(y,",",z,",",x)
if(z<y and z==x):
  print(z,",",x,",",y)

 