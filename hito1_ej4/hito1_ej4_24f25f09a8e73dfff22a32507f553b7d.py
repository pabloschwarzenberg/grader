#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    # Verificar si el número es cero
    if decimal == 0:
        return "0"
    
    # Realizar la conversión a binario
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    
    return binario

# Solicitar al usuario ingresar el número decimal
decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado = decimal_a_binario(decimal)

# Mostrar el resultado
print("resultado=" + resultado)