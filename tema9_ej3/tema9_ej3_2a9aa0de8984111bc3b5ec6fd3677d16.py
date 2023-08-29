def decodificar(mensaje):
	numeros_binarios=mensaje.split(",")
	letras=[]

	for num_binario in numeros_binarios:
		num_decimal=int(num_binario, 2)
		letra=chr(num_decimal)
		letras.append(letra)

	mensaje_descifrado="".join(letras)
	return mensaje_descifrado

mensaje_cifrado="01101000,01101111,01101100,01100001"
mensaje_descifrado = decodificar(mensaje_cifrado)
print(mensaje_descifrado)  # hola