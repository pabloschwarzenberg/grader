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
    palabras = len(frase.strip().replace("\n", " ").replace("  ", " ").split(" "))
    espacios = frase.count(" ")
    puntuacion = frase.count(".")
    promedio = 0
    frase2 = frase.strip().replace("\n"," ").replace(".", "").replace("  ", " ").split(" ")
    for palabra in frase2:
        promedio += len(palabra)
    print(frase2)
    print(promedio)
    promedio = promedio / len(frase2)
    print(promedio)
    caracteres = len(frase)
    return (palabras, caracteres, promedio, espacios, puntuacion)