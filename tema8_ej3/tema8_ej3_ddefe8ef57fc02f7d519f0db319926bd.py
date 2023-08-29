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
    a = frase.count(" ")
    b = frase.count("\n")
    x = 0
    c = len(frase)
    for i in frase:
        if not i.isalpha():
            x += 1
    x = x -a -b
    alpha = c - a -b - x
    sl = 0
    y = 0
    while y < c:
        if frase[y] == "\n":
            if frase[y + 1] == "\n" or y == 0:
                sl += 1
        y += 1
    palabras = a + b + 1 - sl
    prom = alpha / palabras
    return palabras, c, prom, a, x

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))