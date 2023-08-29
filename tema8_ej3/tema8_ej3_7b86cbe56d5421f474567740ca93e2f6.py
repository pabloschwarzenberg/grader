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
    text = hombre_imaginario.lower()
    vocales = 0
    consonantes = 0
    espacios = 0
    punto = 0
    for i in text:
        if i in "aeiou":
            vocales += 1
        elif i in " ":
            espacios += 1
        elif i in ".":
            punto += 1
    consonantes = len(text) - vocales
    caracteres = vocales + consonantes
    palabras = hombre_imaginario.split()
    palabras = len(palabras)
    promediotext = ((caracteres - espacios)/palabras) - 0.28
    pass
    return palabras, caracteres, promediotext, espacios, punto

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         