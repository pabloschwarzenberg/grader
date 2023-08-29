#Conversión de Decimal a Binario
def decimal_a_binario(d):
    if d <= 0:
        return "0"
    b= ""
    while d > 0:
        residuo = int(d % 2)
        d = int(d / 2)
        b= str(residuo) + b
    return b
d= int(input("Ingresa un número decimal: "))
b= decimal_a_binario(d)
print("resultado=",b)    