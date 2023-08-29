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

def estadisticas_frase(frase):
    c = len(frase)
    numeroespacios  = 0
    numeropuntiacion = 0
    x = " "
    for x in frase:
        if x == " ":
            numeroespacios = numeroespacios + 1
        if x == ".":
            numeropuntiacion = numeropuntiacion +1
    frase = frase.strip(".")
    palabras = len(frase.split())
    
    l_prom = list(frase.split())
    sumatoria = 0
    suma = 0 
    for y in range(palabras):
        sumatoria = len(l_prom[y])
        y = y + 1
        suma = suma + sumatoria
    promedio = suma/palabras
    return palabras, c, promedio, numeroespacios, numeropuntiacion
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))