def validadorSecuencia(secuencia):
	elementos = ["a", "c", "t", "g"]
	aux = secuencia.lower()
	out = "secuencia correcta"
	for i in aux:
		if i not in elementos:
			out = "secuencia incorrecta"
	return out
#sec = input("Ingresa una secuencia: ")
print(validadorSecuencia(input("Ingresa una secuencia: ")))
