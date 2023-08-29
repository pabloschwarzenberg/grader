numero = int(input('Introduce el número a convertir a binario: '))
binario = ''
while numero // 2 != 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
print("resultado =", str(numero) + binario)
