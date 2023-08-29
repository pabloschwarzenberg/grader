#Cajero Automático
usuario=int(input("Ingrese su numero de usuario: "))
intentos=3
saldocj=1000000
saldocu=100000
for a in range(1,intentos+1):
		clave=int(input("Ingrese su clave: "))
		if usuario==10334151 and clave!=1803:
			print("Clave incorrecta ")
		else: 
			print("Tu saldo es: 100.000 ")
			monto=int(input("Ingrese monto a retirar: "))
		saldocu=saldocu-monto	
		saldocj=saldocj-monto
		print("saldo cuenta: " + str(saldocu))
		print("saldo cajero: " + str(saldocj))
print("Tarjeta bloqueada ")
     