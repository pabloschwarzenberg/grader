# por favor escribe aquí tu función
 
def es_primo(num):
	if(num > 1):
		for i in range(2, int(num * 0.5)+1):
			if(num % i == 0):
				return False
	else:
		return False
	return True