#Conversión de Decimal a Binario
def decimal_a_binario(num):
    if num == 0:
        return "0"

    resultado = ""
    while num > 0:
        resultado = str(num % 2) + resultado
        num = num // 2

    return resultado

num_decimal = int(input("Ingresa un número decimal: "))

resultado_binario = decimal_a_binario(num_decimal)

print("resultado =", resultado_binario)