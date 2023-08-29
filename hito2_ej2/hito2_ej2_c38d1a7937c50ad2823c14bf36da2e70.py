def validar(string):
	i = 0
	for i in range(len(string)):
		if string[i] != ('A', 'T', 'G', 'C'):
			return "Secuencia incorrecta"
			break
		else:
			return "Secuencia correcta"

if __name__ == '__main__':
	a = input("Ingrese secuencia: ")
	print(validar(a.upper()))