#Ordenar tres números
# Obtener los números del usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Encontrar el menor número
menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

# Encontrar el mayor número
mayor = num1
if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3

# Encontrar el número del medio
medio = num1
if menor < num2 < mayor:
    medio = num2
elif menor < num3 < mayor:
    medio = num3

# Imprimir los números ordenados
orden = str(menor) + ", " + str(medio) + ", " + str(mayor)
print(orden)