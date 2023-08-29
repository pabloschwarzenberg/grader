#Ordenar tres números

n1 = int(input("ingrese el numero: "))
n2 = int(input("ingrese el numero: "))
n3 = int(input("ingrese el numero: "))

# mayor

if n1 > n2 and n1 > n3:
    mayor = n1

elif n2 > n1 and n2 > n3:
    mayor = n2

else:
    mayor = n3

# menor

if n1 < n2 and n1 < n3:
    menor = n1

elif n2 < n1 and n2 < n3:
    menor = n2

else:
    menor = n3

# intermedio

if n2 < n1 < n3 or n2 > n1 > n3:
    intermedio = n1

elif n1 < n2 < n3 or n1 > n2 > n3:
    intermedio = n2

else:
    intermedio = n3

# resultado
print(menor, ",", intermedio, ",", mayor)
