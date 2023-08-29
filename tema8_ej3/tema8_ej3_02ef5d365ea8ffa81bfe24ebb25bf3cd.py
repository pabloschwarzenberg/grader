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

texto =  'hola hola!'

# Numero de palabras
# Numero de caracteres
# Largo promedio de las palabras
# Numero de espacios
# Numero de caracteres de puntuacion

def estadisticas_frase(frase):

    frase_list = frase.split()
    numero_de_palabras = len(frase_list)

    numero_de_caracteres = len(frase)

    espacios = 0
    for letra in frase:
        if letra == ' ':
            espacios += 1

    puntuacion = 0
    for letra in frase:
        if letra == '.' or letra == ',' or letra == '!' or letra == '?' or letra == '¿' or letra == '¡':
            puntuacion += 1

    letras = 0
    for letra in frase:
        if letra.isalpha():
            letras += 1

    largo_promedio = letras/numero_de_palabras
    return numero_de_palabras, numero_de_caracteres, largo_promedio, espacios, puntuacion

print(estadisticas_frase(hombre_imaginario))