#Cajero Automático

ATMBalance=1000000
uBalance=100000
out = []
bills = [20000, 10000, 5000]

sec=True
request=True
block=0
uknuser = True

while(uknuser):
	uc = int(input("Ingrese usuario: "))
	if(uc == 10334151):
		uknuser = False


while(sec and block < 3):
	password = input("Ingrese contraseña: ")
	if(password == '1803'):

		sec = False
	else:
		print("clave invalida")
		block += 1

if (block == 3):
	print("tarjeta bloqueada")
	quit()


else:
	while request:
		amnt = int(input("Ingrese monto a retirar: "))
		if(amnt > uBalance):
			print("monto no permitido")
		else:
			request = False
			for i in bills:
				a = amnt // i
				amnt -= a*i
				uBalance -= a*i
				ATMBalance -= a*i
				out.append(a)
				if (amnt == 0):
					break
			print('saldo cuenta=', uBalance, 'saldo cajero=', ATMBalance)
			for j in range(len(out)):
				print('billetes', bills[j], '=', out[j])