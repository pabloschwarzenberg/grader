# completa el código de la función
def amigos(a,b):
	
	suma1=sum(divisor for divisor in range(1, a) if a % divisor == 0)
	suma2=sum(divisor for divisor in range(1, b) if b % divisor == 0)

	if suma1==b and suma2==a:
		return True
	else:
		return False

n1=int(17)
print('')
n2=int(18)
print('')

if amigos(n1, n2):
    print('Los numeros ', n1, ' y ', n2, ' son amigos.')

else:
    print('Los numeros ', n1, ' y ', n2, ' no son amigos.')
           