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
    caracteres_frase = list(frase)
    versos = frase.replace(".", "").split("\n")
    palabras_frase = []
    sum_len_palabras = 0
    for verso in versos:
        for palabra in verso.split(' '):
            if(palabra != ' ' and palabra != ''):
                palabras_frase.append(palabra)
                sum_len_palabras += len(palabra)

    count_espacios = 0
    count_letras = 0
    count_puntuacion = 0
    for caracter in caracteres_frase:
        if caracter == ' ':
            count_espacios +=1
        elif caracter == '.' or caracter == ',' or caracter == ';' or caracter == ':':
            count_puntuacion +=1
        else:
            count_letras +=1

    return (len(palabras_frase), len(caracteres_frase), sum_len_palabras/len(palabras_frase), count_espacios, count_puntuacion)
