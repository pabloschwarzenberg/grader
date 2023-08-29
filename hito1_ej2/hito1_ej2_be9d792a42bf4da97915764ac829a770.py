#Contestador de celular
while True:
	
	tel=input("Ingrese un numero de telefono de 8 Digitos : ")
	hora=int(input("Ingrese hora de llamada :  "))
	
	if len(tel) >7 and len(tel) <= 8:
		prefijo=tel[0:3]
		sufijo=tel[5:8]
		if (hora >= 0) and (hora<=7):
			print("CONTESTAR")
		elif (hora > 7) and (hora<=14) and (sufijo=="909"):
			print("CONTESTAR")
		elif (hora > 17) and (hora<=19) and (prefijo != "877"):
			print("CONTESTAR")
		else:
			print("NO CONTESTAR")
			
		break
		
	else:
		print("Ingrese un numero de 8 digitos porfavor")      