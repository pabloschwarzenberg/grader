#Conversión de Decimal a Binario
      def decimal_a_binario(numero_decimal):
    if numero_decimal == 0:
        return "0"

    binario = ""
    while numero_decimal > 0:
        residuo = numero_decimal % 2
        binario = str(residuo) + binario
        numero_decimal //= 2

    return binario

numero_decimal = int(input("Ingrese un número decimal: "))

resultado = decimal_a_binario(numero_decimal)

print("resultado=" + resultado)