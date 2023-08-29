#Conversión de Decimal a Binario
def binarizar(decimal_):
    binario = ''
    while decimal_ // 2 != 0:
        binario = str(decimal_ % 2) + binario
        decimal_ = decimal_ // 2
    return str(decimal_) + binario

num = int(input('Introduce número a convertir a binario: '))
print("resultado=",binarizar(num))