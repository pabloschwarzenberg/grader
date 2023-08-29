def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    lineas = archivo.readlines()
    lineas = list(map(lambda x: x.rstrip("\n"), lineas))
    lineas = list(map(lambda x: x.lower(), lineas))
    lineas = list(map(lambda x: x.replace(" ", ""), lineas))
    lista = []
    S = "".join(lineas)
    verticales = []
    for k in range(0,4):
        t = S[k]+S[k+4]+S[k+8]
        verticales.append(t)
    diagonales = []
    for n in range(0,2):
        u = S[n]+S[n+5]+S[n+10]
        diagonales.append(u)

    for i in range(0, len(palabras)):
        palabra = palabras[i]
        for j in range(0, len(lineas)):
            if lineas[j].find(palabra) != -1:
                fila_1 = j
                columna_1 = lineas[j].find(palabra)
                coordenadas = [fila_1, columna_1]
                orientacion = "derecha"
                lista.append((palabra, coordenadas, orientacion))
               
        for m in range(0, len(verticales)):
            if verticales[m].find(palabra) != -1:
                fila_1 = verticales[m].find(palabra)
                columna_1 = m
                coordenadas = [fila_1, columna_1]
                orientacion = "abajo"
                lista.append((palabra, coordenadas, orientacion))

        for o in range(0, len(diagonales)):
            if diagonales[o].find(palabra) != -1:
                fila_1 = diagonales[0].find(palabra)
                columna_1 = o
                coordenadas = [fila_1, columna_1]
                orientacion = "diagonal"
                lista.append((palabra, coordenadas, orientacion))
       
    archivo.close()
    return lista
   
if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))


if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)

           