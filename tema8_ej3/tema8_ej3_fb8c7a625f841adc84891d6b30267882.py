import re
import statistics

def estadisticas_frase(s):
   
    regex = r'\b\w+\b'
    words = re.findall(regex,s)

    word_number = len(words)
    lengths = list(map(lambda word: len(word), words))
   
    average = statistics.mean(lengths)
    space_number = len(re.findall(r" ", s))
    break_number = len(re.findall(r"\n", s))
    character_number = len(s)

    punctuation_number = character_number - space_number - sum(lengths) - break_number

    return word_number,character_number, average, space_number, punctuation_number


poem = """
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

print(estadisticas_frase(poem))