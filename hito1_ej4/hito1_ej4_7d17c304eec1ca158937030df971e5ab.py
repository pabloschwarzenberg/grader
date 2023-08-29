#Conversión de Decimal a Binario
NumeroDecimal=int(input('Ingrese un numero decimal: '))

NumeroBinario=int(bin(NumeroDecimal)[2:])

N=str(NumeroBinario)
print('')

print('resultado=',N)      