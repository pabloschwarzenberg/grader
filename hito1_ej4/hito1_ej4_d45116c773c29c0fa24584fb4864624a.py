numero_decimal = int(input("Ingrese un número decimal: "))

# Verificar si el número es cero
if numero_decimal == 0:
    resultado = "0"
else:
    resultado = ""
    # Realizar la conversión a binario
    while numero_decimal > 0:
        residuo = numero_decimal % 2
        resultado = str(residuo) + resultado
        numero_decimal = numero_decimal // 2

print("resultado=" + resultado)
