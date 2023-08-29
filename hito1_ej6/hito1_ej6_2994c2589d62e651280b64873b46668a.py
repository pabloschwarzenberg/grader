#Ordenar tres números
x1 = int(input("Ingrese un numero: "))
x2 = int(input("Ingrese un numero: "))
x3 = int(input("Ingrese un numero: "))

if (x1 <= x2) and (x1 <= x3):
    menor = x1
    if (x2 <= x3):
        medio = x2
        mayor = x3
    else:
        medio = x3
        mayor = x2
elif (x2 <= x1) and (x2 <= x3):
    menor = x2
    if (x1 <= x3):
        medio = x1
        mayor = x3
    else:
        medio = x3
        mayor = x1
else:
    menor = x3
    if (x2 <= x1):
        medio = x2
        mayor = x1
    else:
        medio = x1
        mayor = x2
print(menor,",",medio,"," ,mayor)