def suma_de_numeros_naturales(n):
    suma = n * (n + 1) // 2
    return suma

N = int(input("Ingresa un numero natural: "))

resultado = suma_de_numeros_naturales(N)
print("La suma de los " + str(N) + " primeros numeros naturales es: " + str(resultado))