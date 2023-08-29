#Ordenar tres números
a=int(input("#1 - Ingrese un numero: "))
b=int(input("#2 - Ingrese un numero: "))
c=int(input("#3 - Ingrese un numero: "))
if a >= b >= c:
    z=a
    y=b
    x=c
if a >= c >= b:
    z=a
    y=c
    x=b
if b >= a >= c:
    z=b
    y=a
    x=c
if b >= c >= a:
    z=b
    y=c
    x=a
if c >= a >= b:
    z=c
    y=a
    x=b
if c >= b >= a:
    z=c
    y=b
    x=a
print(x,",",y,",",z)