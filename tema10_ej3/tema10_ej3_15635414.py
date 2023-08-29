def BuscaPalabras(texto, palabra):
    # buscar palabras en filas
    filas = texto
    for id_f in range(len(filas)):
        if palabra in filas[id_f]:
            id_c = filas[id_f].find(palabra)
            print("(", palabra, " [", id_f, ",", id_c, "], derecha)", sep='')

    # buscar palabras en columnas

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
            print("(", palabra, " [", id_f, ",", id_c, "], abajo)", sep='')

    # buscar palabras en diagonales

    diagonalSupInf = ""
    diagonalInfSup = ""

    for id_f in range(0, len(filas)):
        diagonalSupInf += filas[id_f][id_f]
        diagonalInfSup += filas[len(filas)-1-id_f][id_f]

    if palabra in diagonalSupInf:
        id_f = id_c = diagonalSupInf.find(palabra)
        print("(", palabra, " [", id_f, ",", id_c, "], diagonal)", sep='')

    if palabra in diagonalInfSup:
        id_c = diagonalSupInf.find(palabra)
        id_f = len(filas)-1-id_c
        print("(", palabra, " [", id_f, ",", id_c, "], diagonal arriba)", sep='')

# Lectura archivo
archivoSerHumano = open("mitablero.txt")
texto = []
for linea in archivoSerHumano:
    linea = linea.strip().replace(" ", "")
    texto.append(linea)
    print(linea)
archivoSerHumano.close()

# Lista de palabras
L = ["casa", "auto", "prueba", "lente", "gato", "lampara",
     "pantalla", "sofa", "cuadro", "radio"]

for p in L:
    BuscaPalabras(texto, p.upper())

           