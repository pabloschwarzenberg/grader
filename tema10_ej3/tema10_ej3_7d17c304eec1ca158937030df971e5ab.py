def sopaletras(nombre_archivo, palabras):
	
	archivo=open(nombre_archivo, "r")
	t=[]
	
	for linea in archivo:
		
		fila=linea.strip().split()
		t.append(fila)
		
	archivo.close()

	r=[]

	filas=len(t)
	columnas=len(t[0])

	for palabra in palabras:
		
		palabra=palabra.upper()
		
		PalabraAcertada=False
		
		for i in range(filas):
			
			for j in range(columnas):
				
				if t[i][j]==palabra[0]:

					if j + len(palabra) <= columnas and all(t[i][j+k] == palabra[k] for k in range(len(palabra))):
						
						r.append((palabra.lower(), [i, j], "derecha"))
						PalabraAcertada = True

					if i + len(palabra) <= filas and all(t[i+k][j] == palabra[k] for k in range(len(palabra))):
						
						r.append((palabra.lower(), [i, j], "abajo"))
						PalabraAcertada = True

					if i + len(palabra) <= filas and j + len(palabra) <= columnas and all(t[i+k][j+k] == palabra[k] for k in range(len(palabra))):
						
						r.append((palabra.lower(), [i, j], "diagonal"))
						PalabraAcertada = True

				if PalabraAcertada:
					
					break
					
			if PalabraAcertada:
				
				break

	return r

if __name__=='__main__':
	
	print(sopaletras("sopa.txt", ["cra"])[0])
	print(sopaletras("sopa.txt", ["aro"])[0])
	print(sopaletras("sopa.txt", ["casa"])[0])
	print(sopaletras("sopa.txt", ["casa", "cra", "aro"]))