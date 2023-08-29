numero = int(input("Ingresa un número de hasta 4 dígitos: "))

U = numero % 10
D = (numero % 100) // 10
C = (numero % 1000) // 100
M = numero // 1000

print('Descomposición:', M, 'M', '+', C, 'C', '+', D, 'D', '+', U, 'U')