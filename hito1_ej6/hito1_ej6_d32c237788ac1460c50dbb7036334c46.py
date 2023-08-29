def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort()
    return numeros

num1 = 52
num2 = 15
num3 = 52

numeros_ordenados = ordenar_numeros(num1, num2, num3)
resultado = ','.join(map(str, numeros_ordenados))
print(resultado)