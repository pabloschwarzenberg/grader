def sopaletras(nombres_archivo, palabras):
    archivo = open(nombres_archivo, "r")
    lista = []
    for linea in archivo:
        limpiar = linea.strip().lower()
        fila = limpiar.split(" ")
        lista.append(fila)
    archivo.close()
    print(lista)
    resultado = []
    k = 0
    mcolumnas = len(lista[0])
    nfilas = len(lista)
    print(palabras[k])
    while k < len(palabras):
        palabra = palabras[k]
        letra = palabras[k][0]
        largo = len(palabras[k])

        i = 0
        posiciones = []

        while i < nfilas:
            j = 0
            while j < mcolumnas:
                if lista[i][j] is letra:
                    posicion = [i, j]
                    posiciones.append(posicion)
                j += 1
            i += 1
        for HD in posiciones:
            f = HD[0]
            c = HD[1]
            posible = ""
            y = 0
            while y < largo:
                if (c + y) < mcolumnas:
                    if lista[f][c + y] is palabras[k][y]:
                        posible += lista[f][c + y]
                else:
                    posible = ""
                y += 1
            print(posible)
            print(str(posible) == (palabras[k]))
            if str(posible) == str(palabras[k]):
                resultado.append([palabras[k], [f, c], "derecha"])
            print(resultado)
        for VAB in posiciones:
            a = VAB[0]
            b = VAB[1]

            posibleVAB = ""
            u = 0
            while u < largo:
                if (a + u) < nfilas:
                    if lista[a + u][b] is palabras[k][u]:
                        posibleVAB += lista[a + u][b]

                else:
                    posibleVAB = ""
                u += 1

            if posibleVAB == palabras[k]:
                resultado.append([palabras[k], [a, b], "abajo"])

        for HI in posiciones:
            p = HI[0]
            q = HI[1]
            posibleHI = ""
            r = 0
            while r < largo:
                if (q - r) >= 0:
                    if lista[p][q - r] is palabras[k][r]:
                        posibleHI += lista[p][q - r]
                else:
                    posibleHI = ""
                r += 1
            if posibleHI == palabras[k]:
                resultado.append([palabras[k], [p, q], "izquierda"])

        for VAR in posiciones:
            x = VAR[0]
            z = VAR[1]
            posibleVAR = ""
            w = 0
            while w < largo:
                if (x - w) >= 0:
                    if lista[(x - w)][z] is palabras[k][w]:
                        posibleVAR += lista[(x - w)][z]
                else:
                    posibleVAR = ""
                w += 1

            if posibleVAR == palabras[k]:
                resultado.append([palabras[k], [x, z], "arriba"])

        for diagonal in posiciones:
            h = diagonal[0]
            t = diagonal[1]
            p_diagonal = ""
            s = 0
            while s < largo:
                if (h + s) < nfilas and (t + s) < mcolumnas:
                    if lista[h + s][t + s] is palabras[k][s]:
                        p_diagonal += lista[h + s][t + s]

                else:
                    p_diagonal = ""
                s += 1

            if p_diagonal == palabras[k]:
                resultado.append([palabras[k], [h, t], "diagonal"])
        k += 1

    listaTuplas = []
    for lista1 in resultado:
        listaTuplas.append(tuple(lista1))
    return listaTuplas

if __name__=="__main__":
    a = input("nore:")
    b = input("lista:")
    c = sopaletras(a, b.split(","))
    print(b.split(","))
    print(c)