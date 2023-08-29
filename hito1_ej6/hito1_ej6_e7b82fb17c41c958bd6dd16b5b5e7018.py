#Ordenar tres números
a=int(input("ingrese un numero: "))
b=int(input("ingrese un numero: "))
c=int(input("ingrese un numero: "))
if (a<=b and a<=c):
    x=a
    if(b<=c):
        y=b
        z=c
        print(x,",",y,",",z)
if (b<=a and b<=c):
    y=b
    if(a<=c):
        x=a
        z=c
        print(y,",",x,",",z)
if (c<=a and c<=b):
    z=c
    if(a<=b):
        x=a
        y=b
        print(z,",",x,",",y)
if (a<=b and a<=c):
    x=a
    if(c<=b):
        z=c
        y=b
        print(x,",",z,",",y)
       