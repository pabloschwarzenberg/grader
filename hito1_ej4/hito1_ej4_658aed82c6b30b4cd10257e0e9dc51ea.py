#Conversión de Decimal a Binario
def decimal_a_binario(num_decimal):
    if num_decimal == 0:
        return "0"
    else:
        num_binario = ""
        while num_decimal > 0:
            rem = num_decimal % 2
            num_binario = str(rem) + num_binario
            num_decimal = num_decimal // 2
        return num_binario
num_decimal = int(input("Ingrese un número decimal: "))
num_binario = decimal_a_binario(num_decimal)
print("resultado=", num_binario)    