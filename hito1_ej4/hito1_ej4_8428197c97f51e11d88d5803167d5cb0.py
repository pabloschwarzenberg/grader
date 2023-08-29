#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    if decimal > 1:
        decimal_a_binario(decimal // 2)
    print(decimal % 2, end='')

decimal = int(input("Introduce un número decimal: "))
decimal_a_binario(decimal)
