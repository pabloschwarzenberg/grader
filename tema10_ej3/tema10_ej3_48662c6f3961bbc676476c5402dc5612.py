def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    sopa = archivo.read().split('\n')
    archivo.close()

    for i in range(len(sopa)):
       sopa[i] = sopa[i].replace(" ", "")

    horizontal = []
    for i in range(len(sopa)):
        horizontal.append(sopa[i])      
    
    
    vertical = []
    for i in range(len(sopa[0])):
        palabra = ""
        for j in range(len(sopa)):
            palabra += sopa[j][i]
        vertical.append(palabra)


    diagonal = []
    for i in range(len(sopa), 0, -1):
        palabra = ""
        for j in range(i):
            palabra += sopa[j][len(sopa) - i + j]

        diagonal.append(palabra)


    resultados = []
    for element in palabras:
        element = element.upper()
        if element in horizontal:
            orientacion = "derecha"
            origen = [0,horizontal.index(element)]

        elif element in vertical:
            orientacion = "abajo"
            origen = [0,vertical.index(element)]

        elif element in diagonal:
            orientacion = "diagonal"
            origen = [diagonal.index(element),0]

        else:
            orientacion = ""
            origen = ""
 
        resultados.append((element.lower(),origen,orientacion))


    return resultados    