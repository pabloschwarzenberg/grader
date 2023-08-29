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

def estadisticas_frase(n):
    palabras = n.strip().split(" ")
    print(palabras)
    caracteres = 0
    for palabra in palabras:
        caracteres += len(palabra)+1
    letras_totales = 0
    for palabra in palabras:
        letras_totales += len(palabra)
    largo_promedio = round(letras_totales/len(palabras),1)
    espacios = len(palabras)-1
    puntuacion = n.count(",") + n.count(".")
    return len(palabras), caracteres, largo_promedio, espacios, puntuacion
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))