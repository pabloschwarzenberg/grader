def suma_divisores(n):
	esPrimo = True
	divisores = [1]
	if n == 1:
		esPrimo = False
		suma = 0
	else:
		for i in range(2, n + 1):
			if n % i == 0:
				divisores.append(i)
				if i == n:
					divisores.remove(i)
		suma = sum(divisores)
		if suma == 1:
			esPrimo = True
		else:
			esPrimo = False

	return suma, esPrimo

if __name__ == '__main__':
	num = int(input("Ingrese numero: "))
	print(suma_divisores(num))
           