#Conversión de Decimal a Binario
def binario(d):
    b = ''
    while d//2 != 0:
        b = str(d%2) + b
        d = d//2
    return str(d)+b

n = int(input('ingresa numero: '))
print('resultado=', binario(n))