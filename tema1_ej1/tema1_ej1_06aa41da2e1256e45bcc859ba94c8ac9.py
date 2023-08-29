#Suma de los N primeros números
def calcular_suma_naturales(n):
    suma = (n * (n + 1)) // 2
    return suma

def imprimir_suma_naturales(suma):
    print("La suma de los N primeros números naturales es:", suma)

# Pedir al usuario que ingrese la cantidad de números N
N = int(input("Ingrese la cantidad de números N: "))

# Calcular la suma de los N primeros números naturales
suma_naturales = calcular_suma_naturales(N)

# Imprimir la suma obtenida
imprimir_suma_naturales(suma_naturales)
