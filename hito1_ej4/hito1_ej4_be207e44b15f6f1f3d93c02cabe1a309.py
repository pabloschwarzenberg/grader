# Pedir al usuario que ingrese un número decimal
decimal = int(input("Ingrese un número decimal: "))

# Inicializar una variable para almacenar el resultado
binario = ""

# Mientras el número decimal sea mayor que cero
while decimal > 0:
  # Obtener el resto de dividir el número decimal por dos
  resto = decimal % 2
  # Agregar el resto al inicio del resultado
  binario = str(resto) + binario
  # Dividir el número decimal por dos y actualizarlo
  decimal = decimal // 2

# Imprimir el resultado
print("resultado=" + binario)
