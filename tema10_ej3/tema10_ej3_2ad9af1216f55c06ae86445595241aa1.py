def sopaletras(nombre_archivo,palabras):
    resultado=[]
    archivo=open(nombre_archivo,"r")
    linea=archivo.readline()
    sopa=[]
    while linea!="":
        datos=linea.split()
        sopa.append(datos)
        linea=archivo.readline()
    archivo.close()
    for x in range(len(palabras)):
        posicion=[]
        dire=""
        for fila in range(len(sopa)):
            palabra_formada=""
            for columna in range(len(sopa[0])):
                palabra_formada=palabra_formada+sopa[fila][columna]
            if palabras[x].upper() in palabra_formada:
                dire="derecha"
                posicion=[fila,palabra_formada.index(palabras[x].upper())]
        for columna in range(len(sopa[0])):
            palabra_formada=""
            for fila in range(len(sopa)):
                palabra_formada=palabra_formada+sopa[fila][columna]
            if palabras[x].upper() in palabra_formada:
                dire="abajo"
                posicion=[palabra_formada.index(palabras[x].upper()),columna]
        palabra_formada=""   
        for fila in range(len(sopa)):
            for columna in range(len(sopa[0])):
                if fila==columna:
                    palabra_formada=palabra_formada+sopa[fila][columna]

        if palabras[x].upper() in palabra_formada:
            dire="diagonal"
            posicion=[palabra_formada.index(palabras[x].upper()),palabra_formada.index(palabras[x].upper())]
        resultado.append((palabras[x],posicion,dire))
    return resultado

