def encontrarCords(sopa,palabras):
    c1=0
    c2=0
    for x in sopa:
        for i in x:
            if i == palabras[0][0]:
                return [c1,c2]
            c2+=1
        c1+=1
def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    lineas = archivo.readlines()
    archivo.close()
    sopa = []
    for palabra in lineas:
        palabra = palabra.strip()
        palabra = palabra.split(' ')
        palabrass = []
        for x in palabra:
            palabrass.append(x.lower())
        sopa.append(palabrass)
    respuesta = []
    for i in range(len(palabras)):
        cords = encontrarCords(sopa,palabras[i])
        c1 = cords[0]
        c2 = cords[1]
        if palabras[i][1] == sopa[c1+1][c2]:
            direccion = "abajo"
        elif palabras[i][1] == sopa[c1-1][c2]:
            direccion = "arriba"
        elif palabras[i][1] == sopa[c1][c2+1]:
            direccion = "derecha"
        elif palabras[i][1] == sopa[c1][c2-1]:
            direccion = "izquierda"
        else:
            direccion = "diagonal"
        respuesta.append((palabras[i],[c1,c2],direccion))
    return respuesta

a = 'sopa.txt'
           
           