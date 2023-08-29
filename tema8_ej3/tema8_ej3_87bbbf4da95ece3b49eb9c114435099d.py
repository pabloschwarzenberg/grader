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

def estadisticas_frase(string):
    alfabeto = "abcdefghijklmnopqrstuvwxyzáéíóú"
    alfabetocont = 0
    cantpal = 0
    cantchar = 0
    espacio = " "
    cantespa = 0
    charpunt = ".,;:\"\'()[]{}¿?!¡-"
    cantpunt = 0
    parapalabra = string.split()
    for char in string:
        cantchar += 1
        if espacio in char:
            cantespa += 1
        elif char in charpunt:
            cantpunt += 1
        elif char.lower() in alfabeto:
            alfabetocont += 1
    for cont in parapalabra:
        cantpal += 1
    promedio = alfabetocont/cantpal
    return cantpal, cantchar, promedio, cantespa, cantpunt
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         