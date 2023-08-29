#Conversión de Decimal a Binario
def conversor(deci):
    bina = ''
    while deci // 2 != 0:
        bina = str(deci % 2) + bina
        deci = deci // 2
    return str(deci) + bina

num1=int(input("Introduce el número a convertir a binario: "))
print("resultado=",conversor(num1))