#Suma de los N primeros números
  
def suma_n_primeros_numeros(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

# Solicitar el número al usuario
N = int(input("Ingrese un número entero positivo: "))

# Calcular la suma de los N primeros números naturales
resultado = suma_n_primeros_numeros(N)

# Imprimir el resultado
print("La suma de los", N, "primeros números naturales es:", resultado)
 
 