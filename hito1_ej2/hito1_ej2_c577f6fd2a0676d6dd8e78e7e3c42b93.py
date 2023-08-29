#Contestador de celular
numero_telefonico=(input("Ingrese numero telefonico: "))
hora_llamada=int(input("Ingrese hora de la llamada: "))


if 0<=hora_llamada<=7:
	print("CONTESTAR")

elif 7<hora_llamada<14:
	if numero_telefonico[-3:]=="909":
		print("CONTESTAR")
	else:
		print("NO CONTESTAR")

elif 14<=hora_llamada<17:
	print("CONTESTAR")

elif 17<=hora_llamada<=19:
	if numero_telefonico[:3]=="877":
		print("NO CONTESTAR")
	else:
		print("CONTESTAR")

else:
	print("NO CONTESTAR")     