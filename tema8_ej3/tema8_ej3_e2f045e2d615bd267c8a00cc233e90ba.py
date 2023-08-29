import string
frase = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que rep"""

def estadisticas_frase(frase):
    t_words=0
    puntos=0
    t_char=0
    pprom=0
    t_char += len(frase)
    espacio= frase.count(' ')
    words = frase.split()
    t_words = len(words)
    for word in words:
        wop = word.strip(string.punctuation)
        pprom+=len(wop)
        puntos += len(word) - len(wop)
    promedio= pprom / t_words
    return t_words, t_char, promedio, espacio, puntos
resultado = estadisticas_frase(frase)