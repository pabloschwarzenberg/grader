#Suma de los N primeros números
def suma_n_primeros_numeros(n):
    suma = n*(n+1)/2
    return suma

N = int(input("Ingrese el valor de N: "))
print("La suma de los primeros", N, "números naturales es:", suma_n_primeros_numeros(N))
