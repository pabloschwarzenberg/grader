#Conversión de Decimal a Binario
numero = int(input('Ingrese numero'))
numeroBinario = ''
while(numero>0):
    print(numero)
    if (numero%2==0):
        numeroBinario = str(0)+numeroBinario
    else:
        numeroBinario = str(1)+numeroBinario
    numero = numero//2
print('resultado=', numeroBinario)      