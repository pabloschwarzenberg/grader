#Conversión de Decimal a Binario
def convierte_binario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input("Número a convertir: "))
print("resultado=" , convierte_binario(numero))     