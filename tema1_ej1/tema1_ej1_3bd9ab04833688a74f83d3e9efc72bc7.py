#Suma de los N primeros números
     # Solicitar al usuario ingresar el número N
numero = int(input("Ingrese un número: "))

# Calcular la suma de los N primeros números naturales
suma = sum(range(1, numero + 1))

# Imprimir el resultado
print("La suma de los", numero, "primeros números naturales es:", suma)
