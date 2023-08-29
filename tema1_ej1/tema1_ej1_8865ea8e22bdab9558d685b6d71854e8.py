#Suma de los N primeros números
def suma_numeros_naturales(n):
    suma = (n * (n + 1)) / 2
    return int(suma)
N = int(input("Ingrese el valor de N: "))
suma_total = suma_numeros_naturales(N)
print("La suma de los", N, "primeros números naturales es:", suma_total)      