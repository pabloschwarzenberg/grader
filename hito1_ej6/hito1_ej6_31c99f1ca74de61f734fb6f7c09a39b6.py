numeros = []
for i in range(1,4):
    number = int(input())
    numeros.append(number)

n = len(numeros)
for i in range(n):
    for j in range(0, n-1):
        if numeros[j] > numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

print(numeros)