def numero_perfecto(n):
	suma = 0
	for i in range(1,n):
		if (n % (i) == 0):
			suma += (i)
	if n == suma:
		return True
	else:
		return False
if __name__=="__main__":
  n = int(input("introduzca un numero: "))
print("numero_perfecto(n)")