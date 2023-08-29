def buscarTodas(a,b):
	pos = ""
	for i in range(len(a)):
		if a[i] == b:
			pos += str(i) + " "
	return pos.strip()

if __name__ == "__main__":
	a = str(input("Ingrese string: "))
	b = str(input("Ingrese para buscar: "))
	a.lower()
	b.lower()
	print(buscarTodas(a,b))
           