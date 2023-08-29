#Cajero Automático


saldo_us=100000
saldo_caj=1000000
intento=1
monto=0
salir="N"
b20=20
b10=40
b5=40
sw=1
tarje_bloc = 1
while salir=="N" and tarje_bloc != 0:
	if sw ==1:
		usuario=input("Ingrese usuario : ")
		clave=input("Ingrese Clave : ")

	if usuario=="10334151" and clave=="1803":
		sw=0
		monto = int(input("Ingrese monto a retirar: "))
		if monto > saldo_us or monto > saldo_caj:
			print("monto no permitido")
		else:
			
			saldo_us = saldo_us - monto
			saldo_caj = saldo_caj - monto
			print("saldo cuenta=",saldo_us)
			print("saldo cajero=",saldo_caj)
			bill_20=int(monto/20000)
			monto= monto - (20000*bill_20)
			bill_10=int(monto/10000)
			monto= monto - (10000*bill_10)
			bill_5=int(monto/5000)
			monto= monto - (5000*bill_5)
			if bill_20 >0:
				print("billetes 20000=",bill_20)
				b20=b20-bill_20
			if bill_10 >0:
				print("billetes 10000=",bill_10)
				b10=b10-bill_10
			if bill_5 >0:
				print("billetes 5000=",bill_5)
				b5=b5-bill_5
			
	else:
		print("clave invalida")	
		intento +=1
		sw=1
		if intento > 3:
			print("tarjeta bloqueada")
			tarje_bloc=0
			break

	salir=input("Desea salir: ")
	salir=salir.upper()