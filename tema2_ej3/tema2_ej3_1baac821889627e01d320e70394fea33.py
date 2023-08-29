def Numero_perfecto(a):
	suma = 0
	for i in range(1,a):
		if (a % (i) == 0):
			suma += (i)
	if a == suma:
		return True
	else:
		return False
 
a = int(input("introduzca un numero: "))
if Numero_perfecto(a):
	print("Su numero no es un numero perfecto")
else:
	print("NO es un numero perfecto")

