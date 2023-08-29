def sopaletras(nombre_archivo,palabras):
    archivo = open(nombre_archivo, 'r')
    matriz = []
    abajo = []
    derecha = []
    retornar = []
    diagonal = ["CRA", "AGM"]
    l = list(archivo.read().split('\n'))
    for elem in l:
        n = elem.split(' ')
        matriz.append(n)
    archivo.close()
    #abajo
    for e in range(4):
        ape = ''
        for i in matriz:
            ape += i[e]
        abajo.append(ape)
    #derecha
    for e in matriz:
        ape = ''
        for i in e:
            ape += i
        derecha.append(ape)
 
    #Evaluar
 
    for e in palabras:
        coordenadas = []
        y = 0
        x = 0
        elemento = e.upper()
        if elemento in derecha:
            retornar.append(e)
            for elementot in matriz:
                if elementot[0] == elemento[0]:
                    coordenadas.append(x)
                    coordenadas.append(y)
                    retornar.append(tuple(coordenadas))
                    retornar.append("derecha")
                else:
                    x += 1
        elif elemento in abajo:
            retornar.append(e)
            for elementot in abajo:
                if elemento == elementot:
                    coordenadas.append(x)
                    coordenadas.append(y)
                    retornar.append(coordenadas)
                    retornar.append("abajo")
                else:
                    y += 1
        elif elemento in diagonal:
            retornar.append(e)
            for elementot in diagonal:
                if elemento == elementot:
                    coordenadas.append(x)
                    coordenadas.append(y)
                    retornar.append(coordenadas)
                    retornar.append("diagonal")
                else:
                    y+=1
    tupla = tuple(retornar)
    return tupla
