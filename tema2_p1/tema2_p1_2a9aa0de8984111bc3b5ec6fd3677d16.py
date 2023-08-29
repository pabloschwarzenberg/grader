# por favor escribe aquí tu función
def es_primo(numero):
	if numero<=1:
		return False
	elif numero==2:
		return True
	elif numero % 2 == 0:
		return False

	divisor = 3
	while divisor * divisor <= numero:
		if numero % divisor == 0:
			return False
		divisor+=2

	return True

numero=int(10)

print('')
print(es_primo(numero))
