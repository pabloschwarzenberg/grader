hombre_imaginario  = """
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
    palabras = frase.split()
    frase_sin_puntos = frase.replace(".","")
    palabras1 = frase_sin_puntos.split()
    longitud_total = sum(len(palabra) for palabra in palabras1)
    largo_promedio = longitud_total/len(palabras1)
    cantidad_puntos = hombre_imaginario.count(".")
    print(len(palabras),len(frase),largo_promedio,frase.count(" "),cantidad_puntos)

print(estadisticas_frase(hombre_imaginario))