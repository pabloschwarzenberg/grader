#Conversión de Decimal a Binario
def cambio_base(decimal, base):
    conversion = ''
    while decimal // base != 0:
        conversion = str(decimal % base) + conversion
        decimal = decimal // base
    return str(decimal) + conversion

numero = int(input("Introduce el número a cambiar de base:"))
base = int(input("Introduce la base:"))
print(cambio_base(numero, base))