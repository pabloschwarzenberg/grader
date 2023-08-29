#Conversión de Decimal a Binario
s = int(input('Ingrese numero: '))
def binario(n):
    r = bin(n)
    r = r[2:]
    return r
print('resultado=', binario(s))