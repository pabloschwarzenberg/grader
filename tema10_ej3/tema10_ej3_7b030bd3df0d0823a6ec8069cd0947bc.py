def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    palabras2 = (list("".join(palabras)))
    palabras3 = "".join(palabras)
    palabras3 = palabras3.strip()
    palabras3 = palabras3.lower()
    lista = []
    direccion = []
    direccion2 = []
    fila_columna = []
    contador = 0
    for linea in archivo:
        datos = linea.strip().split(" ")
        lista.append(datos)
    for i in range(len(lista)):
        for j in range(len(lista[0])):          
            if(palabras2[i] == lista[i][j].lower()):
                contador = contador + 1
                direccion.append(lista[i][j].lower())
                if(contador == 1):
                    fila_columna.append(i)
                    fila_columna.append(j)
                    direccion2.append(i)
                    direccion2.append(i)
                    contador = contador + 1
                elif(direccion[0] == direccion[1]):
                    direccion = direccion[i:-1]
    i = int(fila_columna[0])
    j = int(fila_columna[1])
    print("CONOCERE TU VERDAD CONCHETUAMRE",palabras3)
    if(direccion == palabras2 and fila_columna == direccion2):
        archivo.close()
        return [(palabras3,[i,j],"diagonal")]
    elif(direccion != palabras2 and fila_columna == direccion2):
        archivo.close()
        return [(palabras3,[i,j],"derecha")]
    elif(direccion == palabras2 and fila_columna != direccion2):
        archivo.close()
        return [(palabras3,[i,j],"abajo")]
if __name__=="__main__":
    print(sopaletras("sopa.txt", ["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))