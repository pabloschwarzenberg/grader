# completa el código de la función
def suma_divisores(a):
	suma=0

	for i in range(1, a):
		if a % i == 0:
			suma+=i

	if suma==1:
		return suma, True
	else:
		return suma, False

if __name__ == '__main__':
	
	numero = int(input('Ingrese un numero: '))
	suma, es_primo = suma_divisores(numero)

	print('Suma de los divisores:', suma)
	print('Es primo?', es_primo)