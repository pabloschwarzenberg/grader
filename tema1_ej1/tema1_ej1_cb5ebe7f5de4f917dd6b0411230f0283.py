#Suma de los N primeros números
def suma_n_primeros_numeros(n):
    suma = (n * (n + 1)) / 2
    print("La suma de los primeros", n, "números naturales es:", suma)

N = int(input("Ingrese el valor de N: "))
suma_n_primeros_numeros(N)
