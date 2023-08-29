#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    # Verificar si el número es cero
    if decimal == 0:
        return '0' 
    binario = ''
    while decimal > 0:
        # Obtener el residuo de la división por 2
        residuo = decimal % 2       
        # Agregar el residuo al comienzo del número binario
        binario = str(residuo) + binario     
        # Dividir el número decimal por 2
        decimal = decimal // 2   
    return binario
# Solicitar al usuario ingresar el número decimal
decimal = int(input("Ingrese un número decimal: "))
# Llamar a la función para convertir el número a binario
resultado = decimal_a_binario(decimal)
# Imprimir el resultado
print("resultado=" + resultado)