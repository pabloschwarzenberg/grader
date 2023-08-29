#Suma de los N primeros números
print("¡Bienvenido! \n Menu: \n \t 1.Calcular los primeros n numeros naturales \n \t 2.Salir")
while True:
	opc=input("Opcion: ")
	if opc=="2":
		print("¡Nos vemos!")
		break
	elif opc=="1":
		n=int(input("Suma hasta el numero: "))
		if n>1:
			sum=((n*(n+1))/2)
			print("La suma es: %d" % (sum))
		else:
			print("Valor incorrecto.")
	else:
		print("Opcion incorrecta.")