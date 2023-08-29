#Ordenar tres números
x=int(input("ingrese el primer numero: "))
y=int(input("ingrese el segundo numero: "))
z=int(input("ingrese el tercer numero: "))
if x>y and x>z:
    if y>z:
        print(z,",",y,",",x)
    elif z>y:
        print(y,",",z,",",x)
    if z==y:
        print(z,",",y,",",x)
if y>x and y>z:
    if x>z:
        print(z,",",x,",",y)
    elif z>x:
        print(x,",",z,",",y)
    if z==x:
        print(z,",",x,",",y)
if z>x and z>y:
    if x>y:
        print(y,",",x,",",z)
    elif y>x:
        print(x,",",y,",",z)
    if y==x:
        print(y,",",x,",",z)
if x==y and x>z:
    print(z,",",y,",",x)
if x==y and x<z:
    print(y,",",x,",",z)
if z==x and z>y:
    print(y,",",x,",",z)
if z==y and z<y:
    print(z,",",x,",",y)    