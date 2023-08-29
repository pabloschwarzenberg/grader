#Ordenar tres números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

numeros = [numero1, numero2, numero3]
numeros.sort()

numeros_ordenados = ', '.join(str(num) for num in numeros)

print('Números ordenados:', numeros_ordenados)

