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
    f = frase
    numCaracteres = len(f)
    f = f.strip()
    numEspacios = 0
    for car in f:
        if car == " ":
            numEspacios += 1
    f = f.replace("\n", " ")
    f = f.replace("  ", " ")
    numPuntuacion = 0
    for car in f:
        if car in ".,;:¡!¿?":
            numPuntuacion += 1
    f = f.replace(".", "")
    L = f.split(" ")
    numPalabras = len(L)
    largos = list(map(len,L))
    promLargos = sum(largos)/len(L)
    return numPalabras, numCaracteres, promLargos, numEspacios, numPuntuacion