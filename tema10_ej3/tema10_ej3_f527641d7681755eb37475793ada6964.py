name =[]
def sopaletras(nombre_archivo,palabras):
    archivo = open(nombre_archivo,"r")
    sopa = []
    for linea in archivo:
        linea = linea.replace("\n","")
        lista = linea.split(" ")
        sopa.append(lista)
    resultado = []
    for x in range(0,len(sopa)):
        palabra_horizontal = ""
        palabra_diagonal = ""
        for y in range(0,len(sopa[x])):
            palabra_horizontal += sopa[x][y]
            if x + y < len(sopa):
                palabra_diagonal += sopa[x+y][y]

        for palabra in palabras:
            posicion = palabra_horizontal.upper().find(palabra.upper())
            if posicion >= 0:
                resultado.append((palabra,[x,posicion],"derecha"))
            posicion = palabra_diagonal.upper().find(palabra.upper())
            if posicion >= 0:
                resultado.append((palabra,[x + posicion,posicion],"diagonal"))
    for y in range(0,len(sopa[0])):
        palabra_vertical = ""
        for x in range(0,len(sopa)):
            palabra_vertical += sopa[x][y]
        for palabra in palabras:
            posicion = palabra_vertical.upper().find(palabra.upper())
            if posicion >= 0:
                resultado.append((palabra,[posicion,y],"abajo"))


    archivo.close()
    return resultado

if name=="main":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           