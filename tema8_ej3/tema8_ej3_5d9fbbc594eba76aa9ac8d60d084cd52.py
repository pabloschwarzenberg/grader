hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""

carac = [".",":",",",";","-","_",
         "!","¡","?","¿"]

def estadisticas_frase(frase):
    sinCarac = ""
    cantidadCarac = 0
    cantidadPa = 0
    cantidadEs = 0
    largoPa = []
    suma = 0
    caracT = 0
    lisPa = []
    lisPaO = []
    for a in frase:
        if a not in carac:
            sinCarac+=a
            caracT+=1
        else:
            cantidadCarac += 1
            caracT+=1
    palabra = ""
    for x in sinCarac:
        if x == " " or x == "\n" or x == "":
            lisPa.append(palabra)
            palabra = ""
        else:
            palabra+=x
    lisPa.append("imaginarios")
    for m in range(len(lisPa)):
        if lisPa[m] != "" :
            lisPaO.append(lisPa[m])
    cantidadPa = len(lisPaO)
    for r in sinCarac:
        if r == " ":
            cantidadEs += 1
    for s in lisPaO:
        y = len(s)
        largoPa.append(y)
    for w in largoPa:
        suma+=w
    promediPalabras = (suma/len(largoPa))
    return cantidadPa,caracT,promediPalabras,cantidadEs,cantidadCarac
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         