def amigos(a,b):
	
	sumadivisoresa=sum(divisor for divisor in range(1, a) if a % divisor == 0)
	sumadivisoresb=sum(divisor for divisor in range(1, b) if b % divisor == 0)

	if sumadivisoresa==b and sumadivisoresb==a:
		return True
	else:
		return False

nro1=int(17)
print('')
nro2=int(18)
print('')

if amigos(nro1, nro2):
    print('Los numeros ', nro1, ' y ', nro2, ' son amigos.')

else:
    print('Los numeros ', nro1, ' y ', nro2, ' no son amigos.')
           