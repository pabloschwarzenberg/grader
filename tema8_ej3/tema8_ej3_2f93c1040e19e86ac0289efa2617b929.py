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
    texto = hombre_imaginario.lower()
    v = 0
    c = 0
    espacios = 0
    puntuacion = 0
    for i in texto:
        if i in "aeiou":
            v += 1
        elif i == " ":
            espacios += 1
        elif i == ".":
            puntuacion += 1
    c = len(texto) - v
    caracter = v + c
    palabra = hombre_imaginario.split()
    palabra = len(palabra)
    promedio = ((caracter - espacios) / palabra) - 0.28
    pass
    return palabra, caracter, promedio, espacios, puntuacion

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         