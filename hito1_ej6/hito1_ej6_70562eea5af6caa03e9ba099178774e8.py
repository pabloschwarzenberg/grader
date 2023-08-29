x1 = int(input("ingrese un numero: "))
x2 = int(input("ingrese un numero: "))
x3 = int(input("ingrese un numero: "))
if (x1 <= x2) and (x1 <=x3):
    menor = x1
    if (x2 <= x3):
        medio = x2
        mayor = x3
    else:
        medio = x3
        mayor = x2
elif (x2 <= x1) and (x2 <= x3):
    menor =x2
    if (x1 <= x3):
        medio = x1
        mayor = x2
    elif (x1 == x3):
        mayor = x1
        medio = x3
    elif (x3 == x1):
        mayor = x3
        medio = x1
    else:
        medio = x3
        mayor = x1
else:
    menor = x3
    if(x1 <= x2):
        medio = x1
        mayor = x2
    else:
        medio = x2
        mayor = x1
print("el orden de los numeros de menor a mayor es:",menor, ",", medio, ",", mayor)