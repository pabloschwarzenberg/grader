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
    alfabeto = 'aeiouáéíóúbcdfghjklmnñpqrstvwxyzAEIOUÁÉÍÓÚBCDFGHJKLMNÑPQRSTVWXYZ'
    fraseLista = frase.split(' ')
    # num palabras
    numPalabras = len(fraseLista)
    # num caracteres puntuacion y espacios en blanco
    espaciosBlanco = 0
    c_puntuacion = 0
    letras = 0
    for elemento in frase:
        if elemento in alfabeto:
            letras += 1
        else:
            if elemento == ' ':
                espaciosBlanco += 1
            else:
                c_puntuacion += 1
    # num total caracteres
    totalCaracteres = letras + c_puntuacion
    # promedio largo palabras
    palabrasLimpias = []
    for palabra in fraseLista:
        palabraLimpia = palabra.replace('.','')
        palabrasLimpias.append(palabraLimpia)
    suma = 0
    for palabra in palabrasLimpias:
        suma += len(palabra)
    promedio = suma / len(palabrasLimpias)

    return numPalabras, espaciosBlanco, c_puntuacion, totalCaracteres, promedio
         