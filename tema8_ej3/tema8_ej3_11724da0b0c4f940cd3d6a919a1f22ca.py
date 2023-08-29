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
    C = len(frase)
    NE = 0
    NP = 0
    j = " "
    for j in frase:
        if j == " ":
            NE = NE + 1
        if j == ".":
            NP = NP +1
    frase = frase.strip(".")
    palabras = len(frase.split())
    Pl = list(frase.split())
    sum = 0
    total = 0
    for i in range(palabras):
        sum = len(Pl[i])
        i = i + 1
        total = (total + sum)
    Promedio = (total / palabras)
    return palabras, C, Promedio, NE, NP
 
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         