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


def estadisticas_frase(fras):
    caracter = len(fras)
    num_espacio = 0
    nu_puntiacion = 0
    j = " "
    for j in fras:
        if j == " ":
            num_espacio = num_espacio + 1
        if j == ".":
            nu_puntiacion = nu_puntiacion + 1
    frase = fras.strip(".")
    palabras = len(frase.split())

    l_prom = list(frase.split())
    sumatoria = 0
    suma = 0
    for i in range(palabras):
        sumatoria = len(l_prom[i])
        i = i + 1
        suma = suma + sumatoria
    promedio = suma / palabras
    return palabras, caracter, promedio, num_espacio, nu_puntiacion


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))