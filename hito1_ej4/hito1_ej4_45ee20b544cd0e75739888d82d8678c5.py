decimal = int(input("Ingrese un número decimal: "))

# Inicializar la representación binaria como una cadena vacía
binario = ""

# Caso especial cuando el número decimal es 0
if decimal == 0:
    binario = "0"

# Convertir el número decimal a binario
while decimal > 0:
    # Obtener el residuo de la división por 2
    residuo = decimal % 2

    # Agregar el residuo al inicio de la representación binaria
    binario = str(residuo) + binario

    # Actualizar el número decimal dividiéndolo entre 2
    decimal = decimal // 2

print("resultado =", binario)
