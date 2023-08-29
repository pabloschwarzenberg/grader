def sopaletras(nombre_archivo, palabras):
	
	archivo=open(nombre_archivo, "r")
	tablero=[]
	
	for linea in archivo:
		
		fila=linea.strip().split()
		tablero.append(fila)
		
	archivo.close()

	resultados=[]

	filas=len(tablero)
	columnas=len(tablero[0])

	for palabra in palabras:
		
		palabra=palabra.upper()
		
		palabra_encontrada=False
		
		for i in range(filas):
			
			for j in range(columnas):
				
				if tablero[i][j]==palabra[0]:

					if j + len(palabra) <= columnas and all(tablero[i][j+k] == palabra[k] for k in range(len(palabra))):
						
						resultados.append((palabra.lower(), [i, j], "derecha"))
						palabra_encontrada = True

					if i + len(palabra) <= filas and all(tablero[i+k][j] == palabra[k] for k in range(len(palabra))):
						
						resultados.append((palabra.lower(), [i, j], "abajo"))
						palabra_encontrada = True

					if i + len(palabra) <= filas and j + len(palabra) <= columnas and all(tablero[i+k][j+k] == palabra[k] for k in range(len(palabra))):
						
						resultados.append((palabra.lower(), [i, j], "diagonal"))
						palabra_encontrada = True

				if palabra_encontrada:
					
					break
					
			if palabra_encontrada:
				
				break

	return resultados

if __name__=='__main__':
	
	print(sopaletras("sopa.txt", ["cra"])[0])
	print(sopaletras("sopa.txt", ["aro"])[0])
	print(sopaletras("sopa.txt", ["casa"])[0])
	print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))
	print(sopaletras("sopa.txt", ["CASA", "CRA", "ARO"]))