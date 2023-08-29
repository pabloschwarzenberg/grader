#Conversión de Decimal a Binario
nro = int(input("Ingresa un numero: "))

print( 'resultado={}'.format( str(bin(nro)).replace('0b','') ) )