import re
import statistics

def estadisticas_frase(s):
   
    regex = r'\b\w+\b'
    palabras = re.findall(regex,s)

    numero_palabras = len(palabras)
    largo = list(map(lambda palabra: len(palabra), palabras))
   
    promedio = statistics.mean(largo)
    numero_espacios = len(re.findall(r" ", s))
    break_number = len(re.findall(r"\n", s))
    character_number = len(s)

    numero_puntuaciones = character_number-numero_espacios-sum(largo)-break_number

    return numero_palabras,character_number,promedio,numero_espacios,numero_puntuaciones
    

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

print(estadisticas_frase(hombre_imaginario))