#Conversión de Decimal a Binario
 decimal=int(input("ingresa un numero: "))
print("tu numero binario es: ")

def decimal_a_binario(decimal):
    if decimal <=0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = int(decimal% 2)
        decimal = int(decimal /2)
        binario = str(residuo) + binario
        return binario     