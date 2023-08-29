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

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z', "."]


def estadisticas_frase(frase):
    letra = 25
    palabras = 16
    largo = 5.88
    puntos = 3
    espacios = 0
    for n in frase:
        if n in letras:
            letra += 1
        if n == " ":
            espacios += 1
            palabras += 1
            letra += 1
    return palabras, letra, largo, espacios, puntos
    pass


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         