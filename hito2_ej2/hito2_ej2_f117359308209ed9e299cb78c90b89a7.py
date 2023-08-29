# Pedimos al usuario que ingrese la secuencia de ADN
secuencia = input("Ingrese la secuencia de ADN: ")

# Convertimos la secuencia a mayúsculas para hacer la comparación
secuencia = secuencia.upper()

# Definimos el conjunto de bases nitrogenadas válidas
bases_validas = set(["A", "C", "T", "G"])

# Verificamos que la secuencia contenga solamente bases nitrogenadas válidas
if set(secuencia) <= bases_validas:
    print("secuencia correcta")
else:
    print("secuencia incorrecta")
