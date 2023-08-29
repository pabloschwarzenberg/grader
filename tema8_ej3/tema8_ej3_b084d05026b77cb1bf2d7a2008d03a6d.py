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
    palabras = cuenta_palabras(frase)
    caracteres = cuenta_caracteres(frase)
    largo_avg = largo_palabras_avg(frase)
    espacios = cuenta_espacios(frase)
    caracteres_puntuacion = puntuacion(frase)
    estadisticas= (palabras, caracteres, largo_avg, espacios, caracteres_puntuacion)
    return estadisticas

def cuenta_palabras(frase):
    sentence = frase.split()
    palabras = len(sentence ) 
    return palabras

def cuenta_caracteres(frase):
    n=0
    for caracter in frase:
        n = n+1
    return n

def largo_palabras_avg(frase):
    palabras = cuenta_palabras(frase)
    letras = cuenta_letras(frase)
    prom = letras/palabras
    return prom

def cuenta_espacios(frase):
    espacios = 0
    for letra in frase:
        if letra == " ":
            espacios = espacios + 1
    return espacios

def puntuacion(frase):
    puntos=0
    for letra in frase:
        if letra==".":
            puntos= puntos + 1
    return puntos

def cuenta_letras(frase):
    sentence = frase.split()
    sentence = "".join(sentence)
    n=0
    for letra in sentence:
        if letra== ".":
            continue
        else:
            n = n+1
    return n
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         