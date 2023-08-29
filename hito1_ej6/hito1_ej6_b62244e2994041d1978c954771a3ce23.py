#Ordenar tres números

#Ingreso de nuemeros

x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: "))
z = int(input("Ingrese el tercer numero: "))

menor = 0
medio = 0
mayor = 0

#Calculos y proceso

if (x < y and x < z):
    menor = x
    if (y > z):
        mayor = y
        medio = z
    else:
        mayor = z
        medio = y
elif (y < x and y < z):
    menor = y
    if (x > z):
        mayor = x
        medio = z
    else:
        mayor = z
        medio = x
else:
    menor=z
    if (x > y):
        mayor = x
        medio = y
    else:
        mayor = y
        medio = z

#Resultado y muestra

print(menor,",",medio,",",mayor)