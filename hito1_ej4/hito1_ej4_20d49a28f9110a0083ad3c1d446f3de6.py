#Conversión de Decimal a Binario
def decimal_binario(n_decimal):
    if n_decimal <= 0:
        return "0"
    n_binario = ""
    while n_decimal > 0:
        n_residuo = int(n_decimal % 2)
        n_decimal = int(n_decimal / 2)
        n_binario = str(n_residuo) + n_binario
    return n_binario

n_decimal = float(input("Ingrese un número decimal: "))
n_binario = decimal_binario(n_decimal)
print("resultado=", n_binario)