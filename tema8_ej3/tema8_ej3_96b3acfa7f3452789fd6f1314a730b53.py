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

def estadisticas_frase(f):
    t = hombre_imaginario.lower()
    v = 0
    c = 0
    e = 0
    p = 0
    for i in t:
        if i in "aeiou":
            v += 1
        elif i == " ":
            e += 1
        elif i == ".":
            p += 1
    c = len(t) - v
    ca = v + c
    pa = hombre_imaginario.split()
    pa = len(pa)
    pr = ((ca - e) / pa) - 0.28
    pass
    return pa, ca, pr, e, p

if __name__ == "main":
    print(estadisticas_frase(hombre_imaginario))