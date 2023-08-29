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
    car=hombre_imaginario.split()
    numero_palabras=len(car)
    numero_car=len(hombre_imaginario)
    numero_=hombre_imaginario.count(" ")
    numero_puntos=hombre_imaginario.count(".")
    promedio=(numero_car-numero_-numero_puntos-18)/numero_palabras

    return numero_palabras, numero_car, promedio, numero_, numero_puntos

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         