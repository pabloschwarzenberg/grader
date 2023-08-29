#programa que suima n números naturales

# Solicitar el número al usuario
N = int(input("Ingresa un número Natural: "))

# Calcular la suma de los N primeros números naturales
suma_naturales = 0
for i in range(1, N+1):
    suma_naturales = suma_naturales + i

# Imprimir la suma obtenida
print(f"La suma de los {N} primeros números naturales es: {suma_naturales}")
      