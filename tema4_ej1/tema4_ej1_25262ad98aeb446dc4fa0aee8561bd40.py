import random


def ocultar_letras(palabra, cantidad):
    indices = []
    out = ""
    for i in range(cantidad):
        index = random.randint(0, len(palabra) - 1)
        if index not in indices:
            indices.append(index)
        else:
            while index in indices:
                index = random.randint(0, len(palabra) - 1)
            indices.append(index)

    indices.sort()
    print(indices)

    for i in range(0, len(palabra)):
        if i in indices:
            out = out + "_"
            indices.remove(i)
        else:
            out = out + palabra[i]
    return out


def revisar_letra(palabra_secreta, palabra, letra):
	aux = palabra_secreta
	out = palabra
	
	for i in palabra_secreta:
		if i == letra:
			posicion = aux.index(i)
			aux = aux[:posicion] + "_" + aux[posicion+1:]
			out = out[:posicion] + letra + out[posicion+1:]

	return out
