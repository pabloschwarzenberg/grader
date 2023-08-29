#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    if decimal <=0:
       return "0"
    bin_ = ""
    while decimal > 0:
            resto = int(decimal % 2)
            decimal = int(decimal / 2)
            bin_ = str(resto) + bin_
    return bin_

decimal = int(input("Ingresa un número decimal: "))
bin_ = decimal_a_binario(decimal)
print("resultado =",bin_)      