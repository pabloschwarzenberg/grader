#Cajero Automático
sCa = 1000000
sCu = 100000
cuenta1 = ["10334151","1803"]
inicio = []
mR = 0
contadorI = 0
salir = "N"
#inicio.append(str((input("Ingrese su numero de cuenta: ")))
inicio.append("10334151")
inicio.append(str(input("Ingrese su clave: ")))

while(salir == "N") :
	if(contadorI == 3) :
		print("Targeta bloqueada")
		salir = ""
	elif(contadorI < 3) :
		if (inicio != cuenta1) :
			contadorI += 1
			inicio = []
			inicio.append("10334151")
			inicio.append(str(input("Ingrese su clave: ")))
		elif (inicio == cuenta1) :
			mR = int(input("Ingrese monto a retirar: "))
			if (mR > sCa and mR > sCu): 
				print("Monto invalido")
				salir = input("Si quiere salir ingrese una letra distinta de N: ")
			elif(mR <= sCa and mR <= sCu) :
				sCa -= mR
				sCu -= mR
				print("saldo cuenta=",sCu)
				print("saldo cajero=",sCa)
				salir = input("Si quiere salir ingrese una letra distinta de N: ")
	else:
		print("error")
		salir = ""