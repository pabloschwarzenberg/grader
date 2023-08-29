def jerigonzo(string):
	vocales = ["a", "e", "i", "o", "u"]
	aux = string
	out = string
	
	for i in string:
		if i in vocales:
			posicion = aux.index(i)
			out = out[:posicion+1] + "p" + i + aux[posicion+1:]
			aux = aux[:posicion] + "___" + aux[posicion+1:]


	return out