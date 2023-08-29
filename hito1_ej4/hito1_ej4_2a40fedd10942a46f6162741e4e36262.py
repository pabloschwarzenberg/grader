#Conversión de Decimal a Binario
numero_decimal = int(input("Ingrese un número decimal: "))

# Verificación de si el número es cero
if numero_decimal == 0:
    resultado = "0"
else:
    resultado = ""
    # Ciclo para convertir a binario
    while numero_decimal > 0:
        resultado = str(numero_decimal % 2) + resultado
        numero_decimal = numero_decimal // 2

print("resultado=" + resultado)      