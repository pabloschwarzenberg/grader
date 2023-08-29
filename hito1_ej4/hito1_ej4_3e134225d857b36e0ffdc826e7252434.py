#Conversor de Decimal a Binario
numero_decimal=int(input("Ingresar numero decimal: "))
def decimal_a_binario(numero_decimal):
    numero_binario = 0
    multiplicador = 1

    while numero_decimal != 0:
        # se almacena el módulo en el orden correcto
        numero_binario = numero_binario + numero_decimal % 2 * multiplicador
        numero_decimal //= 2
        multiplicador *= 10

    return numero_binario

a=decimal_a_binario(numero_decimal)
print("resultado= "+ str(a))