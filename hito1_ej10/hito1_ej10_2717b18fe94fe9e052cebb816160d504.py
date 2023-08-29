#Cajero Automático
      
ATMBalance=1000000
uBalance=100000

sec=True
request=True
block=0

while(sec and block<=3):
	password=input("Ingrese contraseña: ")
	if(password== '1803'):

		sec=False
	else:
		print("clave invalida")
		block+=1

if (block == 3):
	print("tarjeta bloqueada")
	quit()


else:
	while request:
		Balance=int(input("Ingrese monto a retirar: "))
		if(Balance > uBalance):
			print("monto no permitido")
		else:
			request=False
			uBalance -= Balance
			ATMBalance -= Balance
			print("Saldo cuenta=", uBalance)
			print("Saldo cajero=", ATMBalance)