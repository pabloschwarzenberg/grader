num = int(input('Ingresar numero: '))
numero_binario = ''
# este loop corre hasta que el numero sea menor a 2.
while num > 1:
    # armamos el numero binario de der a izq: 0 si el numero de divide enteramente entre 2; de lo contrario 1.
    numero_binario = str(num % 2) + numero_binario
    # con cada iteracion el numero se reduce
    num //= 2
resultado = str(num) + numero_binario
print('resultado = %s'% resultado)