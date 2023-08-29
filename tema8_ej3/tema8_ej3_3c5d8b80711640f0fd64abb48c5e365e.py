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
    total_ch = len(frase)
    letras = 0
    palabras = 0
    espacios = 0
    punct = 0


    frase = frase.split('\n')
    for linea in frase:
        if linea != '':
            linea = linea.split(' ')

            espacios += len(linea) - 1

            for palabra in linea:
                palabras += 1
                for letra in palabra:
                    if letra.isalnum():
                        letras += 1
                    else:
                        punct += 1
    prom = letras / palabras

    return (palabras, total_ch, prom, espacios, punct)