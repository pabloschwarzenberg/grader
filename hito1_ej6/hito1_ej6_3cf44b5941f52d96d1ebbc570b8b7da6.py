#Ordenar números
# Dar a ingresar los tres números enteros al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Comparación y ordenamiento de los números
menor = min(num1, num2, num3)
mayor = max(num1, num2, num3)
medio = (num1 + num2 + num3) - menor - mayor

# Imprimir los números ordenados
print("Los números ordenados de menor a mayor son: ",menor,",",medio,",",mayor,",")