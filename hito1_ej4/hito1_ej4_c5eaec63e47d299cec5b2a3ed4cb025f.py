#Conversión de Decimal a Binario
#ingreso de numero decimal
numero_decimal = int(input("Ingresa un número decimal: "))

# Verificar si el número decimal es 0
if numero_decimal == 0:
    resultado = '0'
else:
    binario = ''
    
    # Convertir el número decimal a binario
    while numero_decimal > 0:
        binario = str(numero_decimal % 2) + binario
        numero_decimal = numero_decimal // 2
    
    resultado = binario

# Imprimir el resultado
print("Resultado =", resultado)
      