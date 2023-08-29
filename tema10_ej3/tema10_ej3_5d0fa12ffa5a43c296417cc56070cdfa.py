def sopaletras(nombre_archivo,palabras):
    lista_de_palabra = list(palabras)
    lista_de_datos = []
    columna0 = []
    columna1 = []
    columna2 = []
    archivo = open(nombre_archivo, 'r')
    cade = []
    hori = ''

    for linea_dato in archivo:
        linea_dato = linea_dato.strip()
        lista = linea_dato.split()
        lista = list(map(str, lista))
        lista_de_datos.append(lista)

    for dato in lista_de_datos[0]:
        columna0.append(dato)
    for dato in lista_de_datos[1]:
        columna1.append(dato)
    for dato in lista_de_datos[2]:
        columna2.append(dato)

    lugar = lista_de_palabra[0]
    revison = lista_de_palabra[1]

    der = 'derecha'
    ab = 'abajo'
    di = 'diagonal'

    if lugar == 'C' or 'c':
        if revison == 'A' or 'a':
            hori = der
            cade = [0, 0]
        if revison == 'E' or 'e':
            hori = ab
            cade = [0, 0]
        if revison == 'R' or 'r':
            hori = di
            cade = [0, 0]

    if lugar == 'A' or 'a':
        if revison == 'R' or 'r':
            hori = ab
            cade = [0, 1]
        if revison == 'S' or 's':
            hori = der
            cade = [0, 2]
        if revison == 'G' or 'g':
            hori = di
            cade = [0, 2]
        if revison == 'H' or 'h':
            hori = ab
            cade = [3, 3]
        if revison == 'M' or 'm':
            hori = der
            cade = [2, 3]

    if lugar == 'S' or 's':
        if revison == 'A' or 'a':
            hori = der
            cade = [2, 3]
        if revison == 'H' or 'h':
            hori = di
            cade = [2, 3]
        if revison == 'G' or 'g':
            hori = ab
            cade = [2, 2]

    if lugar == 'E' or 'e':
        if revison == 'R' or 'r':
            hori = der
            cade = [0, 1]
        if revison == 'I' or 'i':
            hori = ab
            cade = [0, 0]
        if revison == 'O' or 'o':
            hori = di
            cade = [0, 1]

    if lugar == 'R' or 'r':
        if revison == 'G' or 'g':
            hori = der
            cade = [1, 2]
        if revison == 'A' or 'a':
            hori = di
            cade = [1, 2]
        if revison == 'O' or 'o':
            hori = ab
            cade = [1, 1]

    if lugar == 'G' or 'g':
        if revison == 'H' or 'h':
            hori = der
            cade = [2, 3]
        if revison == 'M' or 'm':
            hori = di
            cade = [2, 3]
        if revison == 'A' or 'a':
            hori = ab
            cade = [2, 2]

    if lugar == 'O' or 'o':
        if revison == 'A' or 'a':
            hori = der
            cade = [1, 2]

    if lugar == 'I' or 'i':
        if revison == 'O' or 'o':
            hori = ab
            cade = [0, 1]

    return palabras, cade, hori