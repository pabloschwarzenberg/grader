#Ordenar tres números
# Entradas

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))

# Operaciones
if a <= b and a<=c:
    menor = a
elif b <= a and b <=c:
    menor = b
else:
    menor = c

if a <= b and a >= c:
    menor_2 = a
elif b >= a and b <=c:
    menor_2 = b
else:
    menor_2 = c

if a >= b and a>=c:
    menor_3 = a
elif b >= a and b >= c:
    menor_3 = b
else:
    menor_3 = c
# Salidas
print("Los numeros ordenados de menor a mayor son: ", menor,",", menor_2,",", menor_3,".")