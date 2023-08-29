#Conversión de Decimal a Binario
def deci_a_bina(deci):
    if deci == 0:
        return '0'
    bina = ''
    while deci > 0:
        bina = str(deci % 2) + bina
        deci //= 2
    return bina

num_decimal = int(input("Ingresa un número decimal: "))
num_binario = deci_a_bina(num_decimal)
print("resultado = ", num_binario)