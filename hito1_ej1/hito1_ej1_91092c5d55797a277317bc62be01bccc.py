#Nota final
print("Bienvenido")
while True:
	print("Menu: \n \t 1.Calcular promedio \n \t 2.Salir")
	opc=input("Opcion: ")
	if opc=="2":
		print("¡Nos vemos!")
		break
	elif opc=="1":
		try:
			pt=float(input("Ingrese Nota de Tareas: "))
			pi=float(input("Ingrese Nota de Interrogaciones: "))
			ne=float(input("Ingrese Nota de Examen: "))
			pp=float(input("Ingrese Nota de Presentacion: "))
			prom=float((0.3*pt)+(0.3*pi)+(0.3*ne)+(0.1*pp))
		except ValueError:
			print("Ha ingresa un valor incorrecto")
			continue
		if (pt or pi or ne or pp)<=0.9:
			print("Nota incorrecta.")
		elif prom>=4:
			print("Aprobado con: ", "{0:.1f}".format(prom))
		else:
			print("Reprobado con:", "{0:.1f}".format(prom))
	else:
		print("Opcion invalida.")