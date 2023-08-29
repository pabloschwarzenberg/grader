# completa el código de la función

def suma_divisores(n):
	num = 0
	for i in range(1, n):
		if(n % i == 0):
			num += i
	for i in range(2, n):
		if(n % i == 0):
			return num, False
		else:
			return num, True
	if(n == 1):
		return num, False
	else:
		return num, True


def main():
	n = int(input("Ingrese un número: "))
	print(suma_divisores(n))


if(__name__ == '__main__'):
	main()