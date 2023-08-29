#Conversión de Decimal a Binario
#conversion de decimal a binario 
from os import system
system("cls")

def decimal_a_binario(numero):
    # Verificar si el número es igual a 0
    if numero == 0:
        return "0"

    # Realizar la conversión a binario
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2

    return binario

# Solicitar al usuario ingresar un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número a binario
numero_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("resultado =", numero_binario)      