#Ordenar tres números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

minimo = min(numero1, numero2, numero3)

maximo = max(numero1, numero2, numero3)

intermedio = numero1 + numero2 + numero3 - minimo - maximo

print("Números ordenados de menor a mayor:", minimo, ",", intermedio, ",", maximo)