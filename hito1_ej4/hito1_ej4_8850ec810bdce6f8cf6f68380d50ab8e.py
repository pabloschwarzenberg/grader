numero = int(input("Ingrese numero: "))




alamacenador=[]

while numero>=1:
	operacion = (numero %2)
	alamacenador.append(int(operacion))
	numero = numero /2

conversion = "".join(map(str, alamacenador))

def invertir_cadena(conversion):
	cadena_invertida = ""
	for i in conversion:
		cadena_invertida = i + cadena_invertida
	return cadena_invertida
ejecutor = invertir_cadena(conversion)

print("resultado="+ejecutor)