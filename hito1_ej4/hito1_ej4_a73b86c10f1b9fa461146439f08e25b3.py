#Conversión de Decimal a Binario
numero= int(input("Ingresa decimal a convertir: "))
def convertirDecimalBinario (decimal):
    resultado = ""

    while decimal > 0:
        residuo= decimal % 2
        resultado = resultado +str(residuo)
        decimal = decimal // 2

    return resultado [::-1]

resultado=(convertirDecimalBinario(numero))
print("resultado= ",resultado)