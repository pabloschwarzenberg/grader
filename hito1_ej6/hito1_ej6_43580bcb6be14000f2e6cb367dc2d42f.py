#Ordenar tres números 
x=eval(input("ingrese un numero:"))
y=eval(input("ingrese otro numero:"))
z=eval(input("ingrese otro numero:"))
if (x > y) and (y > z):
   print(z,",",y,",",x)
if (x > z) and (z > y):
   print(y,",",z,",",x)
if (y > x) and (x > z): 
   print(z,",",x,",",y) 
if (y > z) and (z > x):
   print(x,",",z,",",y) 
if (z > x) and (x > y):
   print(y,",",x,",",z) 
if (z > y) and (y > x):
   print(x,",",y,",",z)
if (x == y) and (x > z):
   print(z,",",y,",",x)
if (x == z) and (x > y):
    print(y, ",",z,",",x)
if (x == y) and (x < z):
   print(x,",",y,",",z)
if (x == z) and (x < y):
    print(x, ",",z,",",y)
       