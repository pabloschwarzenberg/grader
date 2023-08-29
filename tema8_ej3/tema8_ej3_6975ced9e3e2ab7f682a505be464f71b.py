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


def estadisticas_frase(h):

    contador_de_palabras = -2
    c=0

    for indice in h:
        if indice == " " or indice == "\n":
            contador_de_palabras += 1
            letra_anterior = h[c-1]
        c += 1


    largo = len(h)

    contador_espacios = 0

    caracteres = 0
    puntuacion = [",","."]
    no_caracteres = 0

    for i in h:
        if i.isalpha()==True:
            caracteres += 1
        if i in puntuacion:
            no_caracteres += 1

    promedio = caracteres/contador_de_palabras

    for indice in h:
        if indice == " ":
            contador_espacios += 1


    return contador_de_palabras , largo ,  promedio , contador_espacios , no_caracteres


