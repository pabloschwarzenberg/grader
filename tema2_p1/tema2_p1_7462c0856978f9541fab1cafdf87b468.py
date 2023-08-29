# por favor escribe aquí tu función
def es_primo(numero):
	numero = abs(int(numero))
	if numero < 2:
		return False
	elif numero == 2:
		return True
	elif numero % 2 == 0:
		return False	
	else:
		for n in range(3, int(numero**0.5)+2, 2):
			if numero % n == 0:
				return n, False
		return True           