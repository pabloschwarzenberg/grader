if "actgacac":
    print("es correcta")
if "actgb":
    print("es incorrecta")
def secuencia(palabra):
	ABC="ACGT"
	abc="acgt"
	contador=0
	for i in range(len(palabra)):
		if palabra[i] in abc or palabra[i] in abc:
			contador+=1
	if contador==int(len(palabra)):
		return "es secuencia"
	return "no es secuenecia"