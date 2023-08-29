#Cajero Automático

clave = 1803
monto_cajero = 1000000
monto_cliente = 0


usuario = int(input("Ingrese Nombre de Usuario: "))
pas = int(input("Ingrese Clave: "))

if usuario == 10334151 and pas == clave:
	monto_cliente = 100000
	while True:
		retiro = int(input("monto a retirar:"))
		if retiro > monto_cliente:
			print("monto no valido")
			retiro = int(input("monto a retirar:"))
		if retiro < monto_cliente:
			monto_cliente = monto_cliente - retiro
			monto_cajero = monto_cajero - retiro
			print("saldo cuenta=",monto_cliente)
			print("saldo cajero=",monto_cajero)
			break

if usuario == 10334151 and pas != clave:
	intentos = 0
	while pas != clave:
		print("clave invalida")
		pas = int(input("Ingrese Clave: "))
		intentos += 1
		if intentos == 2:
			print("tarjeta bloqueada")
			break
		if pas == clave:
			monto_cliente = 100000
			while True:
				retiro = int(input("monto a retirar:"))
				if retiro > monto_cliente:
					print("monto no valido")
					retiro = int(input("monto a retirar:"))
				if retiro < monto_cliente:
					monto_cliente = monto_cliente - retiro
					monto_cajero = monto_cajero - retiro
					print("saldo cuenta=",monto_cliente)
					print("saldo cajero=",monto_cajero)
					break
