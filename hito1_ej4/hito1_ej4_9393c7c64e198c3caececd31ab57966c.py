#Conversión de Decimal a Binario
dec = int(input('Ingrese un numero decimal:'))
bina = bin(dec)
print('resultado={}'.format(bina[2:]))      