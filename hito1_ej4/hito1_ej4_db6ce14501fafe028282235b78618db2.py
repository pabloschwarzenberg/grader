#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    resultado = ""
    while numero > 0:
        resultado = str(numero % 2) + resultado
        numero = numero // 2
    return resultado


# Solicitar al usuario ingresar un número decimal
decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
binario = decimal_a_binario(decimal)

# Imprimir el resultado
print("resultado=" + binario)
     