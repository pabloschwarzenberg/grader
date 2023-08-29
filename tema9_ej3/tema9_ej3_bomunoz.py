def binario(string):
	string=list(string)
	string.reverse()
	x="".join(string)
	print(x)
	print("len= ",len(x))
	sumatoria_i=0

	for i in range(len(x)):
			if int(x[i])==1:
				sumatoria_i+=2**(i)
				print("pase")
	return chr(sumatoria_i)

def decodificar(mensaje):
	lista_palabras=mensaje.split(",")
	lista_letras=map(binario,lista_palabras)
	return "".join(lista_letras)