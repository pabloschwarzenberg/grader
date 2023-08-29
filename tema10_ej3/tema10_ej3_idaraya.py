def sopaletras(nombre_archivo, palabras):

#aquí almacenamos la ubicación de todas las palabras de la lista
    ubicaciones=[]
#iteramos por cada palabra de la lista
    for palabra in palabras:

        palabra=palabra.upper()
        archivo = open(nombre_archivo,"r")
        texto = []
        for linea in archivo:
          linea = linea.strip().replace(" ", "")
          texto.append(linea)
        archivo.close()
        filas = texto
        for id_f in range(len(filas)):
            if palabra in filas[id_f]:
                id_c = filas[id_f].find(palabra)
                print("(", palabra.lower(), ",[", id_f, ",", id_c, "], derecha)", sep='')
                ubicaciones.append((palabra.lower(),[id_f,id_c],"derecha"))
                continue

        columnas = []

        for i in range(0, len(filas[0])):
            columna_i = ""
            for f in filas:
                columna_i += f[i]
            columnas.append(columna_i)

        id_c = 0
        for id_c in range(len(columnas)):
            if palabra in columnas[id_c]:
                id_f = columnas[id_c].find(palabra)
                print("(", palabra.lower(), ",[", id_f, ",", id_c, "], abajo)", sep='')
                ubicaciones.append((palabra.lower(),[id_f,id_c],"abajo"))
                continue

        diagonal_Sup= ""
        diagonal_Inf = ""

        for id_f in range(0, len(filas)):
            diagonal_Sup += filas[id_f][id_f]
            diagonal_Inf+= filas[len(filas)-1-id_f][id_f]

        if palabra in diagonal_Sup:
            id_f = id_c = diagonal_Sup.find(palabra)
            print("(", palabra.lower(), ",[", id_f, ",", id_c, "], diagonal)", sep='')
            ubicaciones.append((palabra.lower(),[id_f,id_c],"diagonal"))
            continue

        if palabra in diagonal_Inf:
            id_c = diagonal_Inf.find(palabra)
            id_f = len(filas)-1-id_c
            print("(", palabra.lower(), ",[", id_f, ",", id_c, "], diagonal)", sep='')
            ubicaciones.append((palabra.lower(),[id_f,id_c],"diagonal"))
            continue

    return ubicaciones

if __name__=="__main__":
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           

