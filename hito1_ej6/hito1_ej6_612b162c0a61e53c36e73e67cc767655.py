#Ordenar tres números
print("Ordenar números enteros")
x=int(input("x:ingrese un número entero cualquiera:"))
y=int(input("y:ingrese un número entero cualquiera:"))
z=int(input("z:ingrese un número entero cualquiera:"))

if x<=y<=z:
    print(x,",",y,",",z)
if x>=y>=z:
    print(z,",",y,",",x)
if y>=x>=z:
    print(z,",",x,",",y)
if y>=z>=x:
    print(x,",",z,",",y)
if z>=x>=y:
    print(y,",",x,",",z)
if x>=z>=y:
    print(y,",",z,",",x)
