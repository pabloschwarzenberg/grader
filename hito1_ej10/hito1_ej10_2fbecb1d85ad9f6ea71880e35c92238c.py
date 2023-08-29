def cajero():
	
	saldo_cuenta=100000
	saldo_cajero=1000000
	intentos=0

	while True:
		
		usuario=input('Ingrese su usuario: ')
		clave=input('Ingrese su clave: ')
		print('')
		
		if usuario=='10334151' and clave=='1803':
			
			print('Inicio de sesion exitoso.')
			print('')
			print('BIENVENIDO')
			saldo_usuario=saldo_cuenta
			print('')
			break
			
		else:
			
			print('Usuario o clave invalidos.')
			intentos+=1
			print('')
			
			if intentos==3:
				
				print('TARJETA BLOQUEADA')
				return

	while True:
		
		monto=int(45000)
		print('')
		
		if monto > saldo_usuario:
			
			print('Monto no permitido. Fondos insuficientes.')
			print('')
			
		elif monto > saldo_cajero:
			
			print('Monto no permitido. Cajero sin suficiente dinero.')
			print('')
			
		else:
			
			saldo_usuario-=monto
			saldo_cajero-=monto
			print('Retiro exitoso.')
			print('')
			print('Saldo cuenta=',saldo_usuario)
			print('')
			print('Saldo cajero=',saldo_cajero)
			print('')

		opcion='N'
		print('')

		if opcion.upper()=='N':
			
			break

cajero()