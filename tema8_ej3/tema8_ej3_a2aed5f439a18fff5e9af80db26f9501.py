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
    from string import ascii_letters
    abecedario = ascii_letters
    palabras = 1
    caracteres = 0
    espacios = 0
    for letra in frase:
        if letra == " ":
            palabras += 1
            espacios += 1
        if letra in abecedario:
            caracteres += 1
    return (palabras, espacios, caracteres)


if __name__ == "__main__":
    frase = hombre_imaginario
    print(estadisticas_frase(frase))

