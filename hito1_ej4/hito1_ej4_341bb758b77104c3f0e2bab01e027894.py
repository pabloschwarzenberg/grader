#Conversión de Decimal a Binario
def ConvertirDecimalaBinario(decimal):
    x = " "
    while decimal > 0:
        y = decimal % 2
        x = x + str(y)
        decimal = decimal // 2
    return x [::-1]
numero = int(input("Ingrese el numero decimal: "))
print("resultado=",ConvertirDecimalaBinario(numero))      