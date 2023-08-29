#Ordenar tres números
x = int(input("Ingrese el primer digito -> "))
y = int(input("Ingrese el segundo digito -> "))
z = int(input("Ingrese el tercer digito -> "))

if(x <= y) and (x <= z):
    if(y <= z):
        print(x, ",", y, ",", z)
    else:
        print(x, ",", z, ",", y)

if(y <= x) and (y <= z):
    if(x <= z):
        print(y, ",", x, ",", z)
    else:
        print(y, ",", z, ",", x)

if(z <= x) and (z <= y):
    if(y <= x):
        print(z, ",", y, ",", x)
    else:
        print(z,",", x, ",", y)