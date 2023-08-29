#Conversión de Decimal a Binario
def decBin(decimal):
    resultado=""

    while decimal>0:
        residuo=decimal%2
        resultado=resultado+str(residuo)
        decimal=decimal//2
    return resultado[::-1]

numero=int(input("  Ingrese el número decimal:"))
print("resultado=",decBin(numero),sep='')           

