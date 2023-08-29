#Conversión de Decimal a Binario
numero= int(input("Ingrese el numero decimal: "))

def decimal_a_binario(decimal):
    if decimal<=0:
        return "0"

    binario=""

    while decimal //2 !=0:
        binario= str(decimal%2) + binario
        decimal= decimal //2

    return print ("resultado=", str (decimal) + binario)

decimal_a_binario(numero)