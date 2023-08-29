#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    # Verificar si el número es 0
    if decimal == 0:
        return '0'
    
    # Inicializar una lista para almacenar los dígitos binarios
    binario = []
    
    # Convertir el número decimal a binario
    while decimal > 0:
        residuo = decimal % 2
        binario.append(str(residuo))
        decimal = decimal // 2
    
    # Invertir la lista de dígitos binarios
    binario.reverse()
    
    # Unir los dígitos binarios en una cadena
    resultado = ''.join(binario)
    
    return resultado


# Solicitar al usuario el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Obtener el resultado de la conversión a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("Resultado =", resultado_binario)
     