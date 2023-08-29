#Conversión de Decimal a Binario
def convertirabinario(decimal):
    binario=""
    while decimal>1:
        binario=str(decimal % 2) + binario
        decimal= decimal // 2
        binario = str(decimal) + binario
    return binario
decimal = int(input("ingrese un numero entero: "))
print("numero binario es : ", convertirabinario(decimal))