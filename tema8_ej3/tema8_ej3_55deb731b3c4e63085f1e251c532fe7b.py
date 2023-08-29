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
    puncList = [".", ";", ":", "!", "?", "/", "\\", ","]
    word = sum([i.strip('.').isalpha() for i in hombre_imaginario.split()])
    ch = len(hombre_imaginario)
    filtered = ''.join(filter(lambda x: x not in '".,;!-', frase))
    words = [word for word in filtered.split() if word]
    average = sum(map(len, words))/len(words)
    spaces = frase.count(' ')
    count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
    frase_punct = count(frase, puncList)
    frase = (word, ch, average, spaces, frase_punct)
    return frase


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
