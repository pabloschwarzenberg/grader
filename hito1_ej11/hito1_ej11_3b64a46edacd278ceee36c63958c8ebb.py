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

def CalculoBilletes (mR) :
	b20 = [20000]
	b10 = [10000]
	b5 = [5000]
	total = []

	cb20 = 20
	cb10 = 40
	cb5 = 40

	b20a = b20 * cb20
	b10a = b10 * cb10
	b5a = b5 * cb5

	contador20 = 0
	contador10 = 0
	contador5 = 0
	
	suma = 0
	
	while(len(b20a) > 0 and mR >= 20000):
		mR = mR - 20000
		total = total + b20
		contador20 += 1
		b20a.remove(20000)
		
	while(len(b10a) > 0 and mR >= 10000):
		mR = mR - 10000
		total = total + b10
		contador10 += 1
		b10a.remove(10000)
		
	while(len(b5a) > 0 and mR >= 5000):
		mR = mR - 20000
		total = total + b5
		contador5 += 1
		b5a.remove(5000)
	
	for i in total :
		suma = suma + i
		
	return(suma,contador20,contador10,contador5)

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
				(a,b,c,d) = CalculoBilletes(mR)
				print("saldo cuenta=",sCu)
				print("saldo cajero=",sCa)
				if(a == mR):
					print("Billetes 20000=",b)
					print("Billetes 10000=",c)
					print("Billetes 5000=",d)
				salir = input("Si quiere salir ingrese una letra distinta de N: ")
	else:
		print("error")
		salir = ""