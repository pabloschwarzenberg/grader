#Conversión de Decimal a Binario
n = eval(input('Ingrese un número para convertirlo a binario: '))

numBinario = ''

while n > 0:
    if n % 2 == 0:
        numBinario = str(0) + numBinario
    else:
        numBinario = str(1) + numBinario
    n = n//2

print('resultado=', numBinario)
