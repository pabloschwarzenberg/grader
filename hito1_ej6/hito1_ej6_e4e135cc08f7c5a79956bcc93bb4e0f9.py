#Ordenar tres números
x=int(input("ingrese un numero 1"))
y=int(input("ingrese un numero 2"))
z=int(input("ingrese un numero 3"))
if((x<=y) and (x<=z)):
  if(y<=z):
    print(x,",",y,",",z)
  elif(z<=y):
    print(x,",",z,",",y)
elif((y<=x) and (y<=z)):
  if (x<=z):
    print(y,",",x,",",z)
  elif(z<=x):
    print(y,",",z,",",x)
elif((z<=x) and (z<=y)):
  if(x<=y):
    print (z,",",x,",",y)
  elif(y<=x):
    print(z,",",y,",",x)
      
          