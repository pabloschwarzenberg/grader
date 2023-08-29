#Contestador de celular
numero = int(input("Ingrese numero: "))
hora = int(input("Ingrese la hora: "))


if hora >= 0 and hora<= 7:
	print("contestar")
elif hora < 14:
	if numero%1000 == 909:
		print("contestar")
	else:
		print("no contestar")
elif hora >= 14 and hora < 17:
	if numero%1000 == 877:
		print("contestar")
	else:
		print("no contestar")
elif hora >= 17 and hora <= 19:
	if numero %1000 == 877:
		print("comtestar")
	else:
		print("no contestar")
else:
	print("no contestar")