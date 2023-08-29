def buscarTodas(a,b):
	out = ""
	aux = a
	indices = [ ]

	if b in a:
		for i in a:
			if i == b:
				posicion = aux.index(b)
				indices.append(posicion)
				aux = aux[:posicion] + "_" + aux[posicion+1:]
	for i in indices:
		out = out + str(i)
		if i != indices[-1]:
			out = out + " "
	return out

print(buscarTodas("tres tristes tigres", "t"))