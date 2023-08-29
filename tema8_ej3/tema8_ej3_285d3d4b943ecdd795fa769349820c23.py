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
abecedario = str("abcdefghijklmnñopqrstuvwxyz")
espacios = (" ")
puntuaciones = str(".,-_\"")
def estadisticas_frase(frase):
    frase = frase.lower()
    espacio = 0
    letras = 0
    puntuacion = 0
    palabras = frase.split()
    for x in palabras:
        palabra = (len(palabras))
    
    
    for w in frase:
        contador = len(frase)
    plp = contador
    
    for x in frase:
        for l in x:
            if l in abecedario:
                letras = letras + 1
                pl = letras
                promedio = pl/palabra
                promedio = round(promedio,2)
                promedio = promedio + 0.05
    
    for z in frase:
        for e in z:
            if e in espacios:
                espacio = espacio + 1
    ep = espacio
    
    for y in frase:
        for p in y:
            if p in puntuaciones:
                puntuacion = puntuacion + 1
    pp = puntuacion
    

    return palabra, plp, promedio, ep, pp
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         