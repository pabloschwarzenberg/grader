def cargar_sopa(nombre_archivo):
	archivo = open(nombre_archivo, "r")

	lineas = archivo.readlines()
	for idx in range(len(lineas)):
		lineas[idx] = lineas[idx].strip().replace(" ","")

	sopa_de_letras = []
	for linea in lineas:
		sopa_de_letras.append(list(linea))
	return sopa_de_letras

def buscar_letra(sopa, letra, offset):
	for j in range(offset[1], len(sopa)):
		for i in range(offset[0], len(sopa[0])):
			if sopa[j][i] == letra:
				return [i,j]
		offset[0] = 0
	return None

def palabra_encontrada(sopa, palabra, posicion):
	if len(palabra) == 1:
		return "derecha"
	for columna in range(max(posicion[0]-1,0), min(posicion[0]+2, len(sopa[0]))):
		for fila in range(max(posicion[1]-1,0), min(posicion[1]+2, len(sopa))):
			if [columna,fila] == posicion:
				continue
			if palabra[1] == sopa[fila][columna]:
				diferencia = [columna - posicion[0], fila - posicion[1]]
				new_columna = columna
				new_fila  = fila
				for letra in palabra[2::]:
					new_columna += diferencia[0]
					new_fila  += diferencia[1]
					if new_fila >= len(sopa) or new_columna >= len(sopa[0]):
						break
					if letra != sopa[new_fila][new_columna]:
						break
				else:
					if diferencia[0] == 0: # Vertical
						return "abajo"
					elif diferencia[1] == 0: # Horizontal
						return "derecha"
					else: # Diagonal
						return "diagonal"
	return ""

def sopaletras(nombre_archivo, palabras):
	resultados = []
	sopa = cargar_sopa(nombre_archivo)

	for palabra in palabras:
		if len(palabra) == 0:
			continue
		buscando = True
		res = [0,0]
		while(buscando):
			res = buscar_letra(sopa,palabra[0],res)
			if res == None:
				buscando = False
			else:
				direccion = palabra_encontrada(sopa,palabra,res)
				if direccion:
					resultados.append((palabra, [res[1],res[0]], direccion))
					buscando = False
				else:
					res[0]+=1
	return resultados