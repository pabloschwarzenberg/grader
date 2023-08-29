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
    palabras = frase.split()
    number_of_words = len(palabras)
    letras = 0
    espacios = 0
    puntuación = 0
    for palabra in palabras:
        for letra in palabra:
            if letra.isalpha():
                letras += 1
            elif letra not in " \n":
                puntuación += 1
    for char in frase:
        if char == " ":
            espacios += 1
    largo_promedio = letras / number_of_words
    return number_of_words, len(frase), largo_promedio, espacios, puntuación
         