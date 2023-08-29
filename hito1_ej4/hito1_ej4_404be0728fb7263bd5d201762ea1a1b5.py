#Conversión de Decimal a Binario
decimal = eval(input("Ingrese el numero: "))
def decimal_binario(decimal):
    if decimal == '':
        return "No se introdujo un numero"
    else:
        numero = int(decimal)
        numero2 = numero // 2
        numero3 =str(numero % 2)
        if numero2 == 0:
            return numero3
        else:
            return decimal_binario(numero2)+numero3
print("Resultado= ",decimal_binario(decimal))

