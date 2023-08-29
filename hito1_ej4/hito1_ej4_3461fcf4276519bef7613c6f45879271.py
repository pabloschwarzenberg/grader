#Conversión de Decimal a Binario
 # Función para convertir decimal a binario
def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    binario = ''
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario

# Solicitar al usuario ingresar un número decimal
numero_decimal = int(input("Ingresa un número decimal: "))

# Convertir el número decimal a binario
numero_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("El número binario es:", numero_binario)
     