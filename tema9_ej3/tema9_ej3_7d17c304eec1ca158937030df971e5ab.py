def decodificar(mensaje):
	numero=mensaje.split(",")
	x=[]

	for y in numero:
		D=int(y, 2)
		L=chr(D)
		x.append(L)

	mensaje="".join(x)
	return mensaje

cifrado="01101000,01101111,01101100,01100001"
mensaje = decodificar(cifrado)
print(mensaje)