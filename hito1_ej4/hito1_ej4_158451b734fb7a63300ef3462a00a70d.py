#Conversión de Decimal a Binario
num = int(input('Ingresa un número: '))
nbin = ''
while (num > 0):

    if (num % 2 == 0):
        nbin = str(0) + nbin
    else:
        nbin = str(1) + nbin        
    num = num//2
print('resultado=', nbin)