x=input("ingrese numero")
x=int(x)
y=input("ingrese numero")
y=int(y)
z=input("ingrese numero")
z=int(z)
if x>y and y>z and x>z:
   print(z,",",y,",",x)
if y>x and x>z and y>z:
   print(z,",",x,",",y)
if z>x and x>y and z>y:
   print(y,",",x,",",z)
if x>z and z>y and x>y:
   print(y,",",z,",",x)
if z>y and y>x and z>x:
   print(x,",",y,",",z)
if y>z and z>x and y>x:
   print(x,",",z,",",y)
if x==y and x>z and y>z:
   print(z,",",y,",",x)
if x==z and x>y and z>y:
   print(y,",",x,",",z)
if z==y and z>x and y>x:
   print(x,",",y,",",z)
