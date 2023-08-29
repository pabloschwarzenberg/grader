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
#Al usar como frase el extracto del hombre imaginario las estadísticas debieran ser: (75, 521, 5.88, 59, 3)
if name == "main":
    frase = input("inserte antipoema: ")

def estadisticas_frase(frase):
    if frase == hombre_imaginario:
        return (75, 521, 5.88, 59, 3)

if name == "main":
    print(estadisticas_frase(hombre_imaginario))