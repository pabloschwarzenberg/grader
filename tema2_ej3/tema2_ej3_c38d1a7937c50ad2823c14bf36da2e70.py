def numero_perfecto(n):
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
		if suma == n:
			return True
		else:
			return False
			

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           