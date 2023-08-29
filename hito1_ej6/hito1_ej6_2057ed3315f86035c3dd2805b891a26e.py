#Ordenar tres números
# Solicitamos los números al usuario
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))
numero3 = int(input("Ingrese el tercer número entero: "))

# Encontramos el número mínimo
minimo = numero1
if numero2 < minimo:
    minimo = numero2
if numero3 < minimo:
    minimo = numero3

# Encontramos el número máximo
maximo = numero1
if numero2 > maximo:
    maximo = numero2
if numero3 > maximo:
    maximo = numero3

# Calculamos el número medio
medio = numero1 + numero2 + numero3 - minimo - maximo

# Imprimimos los números ordenados
print("Números ordenados: " + str(minimo) + ", " + str(medio) + ", " + str(maximo))