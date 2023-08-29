#Conversión de Decimal a Binario
def n_binario(decimal):
    binario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
numero = int(input("Introduce el número a convertir: "))
print("El resultado=" + str (n_binario(numero)))