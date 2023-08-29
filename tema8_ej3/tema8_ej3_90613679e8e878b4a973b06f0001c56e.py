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
    frase_pura = frase.strip('".')

    caracteres = len(frase)

    cantidad_palabras = 0

    frase_lista = frase.split(" ")


    espacios = frase_pura.count(" ")

    puntos = frase.count(".")

    sumaLargos = []


    for i in frase_lista:
        cantidad_palabras += 1
        if "\n" in i:
            cantidad_palabras += 1
    if "\n" in frase_lista[0]:
        cantidad_palabras -= 1

    for i in frase_lista:
        if "\n" in i:
            sumaLargos.append(-1)
        if "." in i:
            sumaLargos.append(-3)
        if "\n\n" in i:
            sumaLargos.append(-1)
        sumaLargos.append(len(i))


    promedios = sum(sumaLargos) / cantidad_palabras





    return(cantidad_palabras, caracteres, promedios, espacios, puntos)
