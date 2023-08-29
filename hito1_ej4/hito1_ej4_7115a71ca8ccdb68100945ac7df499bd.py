#Conversión de Decimal a Binario
def decimal_binario(decimal):
    resultado = " "
    
    while decimal > 0:
        residuo = decimal % 2
        resultado = resultado + str(residuo)
        decimal = decimal // 2
    return resultado [::-1]

numero = int(input("Ingrese el número decimal que desea convertir: "))
print("resultado=" + decimal_binario(numero))