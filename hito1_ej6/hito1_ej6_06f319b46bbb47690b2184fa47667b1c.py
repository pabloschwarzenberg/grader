#Ordenar tres números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

min_num = min(numero1, numero2, numero3)
max_num = max(numero1, numero2, numero3)
mid_num = numero1 + numero2 + numero3 - min_num - max_num

numeros_ordenados = [min_num, mid_num, max_num]

resultado = ', '.join(str(num) for num in numeros_ordenados)
print("Números ordenados de menor a mayor:", resultado)
