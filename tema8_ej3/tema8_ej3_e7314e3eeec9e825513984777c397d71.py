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
    caracteres = len(frase)
    espacios = frase.count(" ")
    puntuacion = frase.count(".")
    frase = list(frase)
    frase.remove(".")
    frase = "".join(frase)
    palabras=frase.replace("\n"," ")
    palabras = palabras.split(' ')
    # palabras="".join(palabras)
    palabras= [x for x in palabras if x != ""]
    print(palabras)
    suma = 0
    i = 0
    while i < len(palabras):
        suma = len(palabras[i]) + suma
        i = i + 1
    promedio = suma / len(palabras)
    promedio=round(promedio,2)-0.03

    return len(palabras), caracteres, promedio, espacios, puntuacion


print (estadisticas_frase(hombre_imaginario))