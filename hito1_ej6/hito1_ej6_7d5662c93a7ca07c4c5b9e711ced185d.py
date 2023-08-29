#Ordenar tres números
# Solicitar al usuario que ingrese los tres números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Encontrar el número menor
menor = numero1
if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3

# Encontrar el número medio
medio = numero1
if menor == numero1:
    if numero2 < numero3:
        medio = numero2
    else:
        medio = numero3
elif menor == numero2:
    if numero1 < numero3:
        medio = numero1
    else:
        medio = numero3
else:
    if numero1 < numero2:
        medio = numero1
    else:
        medio = numero2

# Encontrar el número mayor
mayor = numero1
if mayor == menor:
    mayor = medio
elif mayor == medio:
    mayor = numero3

# Imprimir los números ordenados
print("Números ordenados:", menor, ",", medio, ",", mayor)
