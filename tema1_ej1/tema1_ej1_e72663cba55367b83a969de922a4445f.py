#Suma de los N primeros números
#Pedir al usuario el valor de N
# Calcular la suma de los N primeros números naturales
def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    return suma
    
N = int(input("Ingrese un número N: "))

resultado = suma_n_primeros_numeros(N)

print("La suma de los", N, "primeros números naturales es:", resultado)      