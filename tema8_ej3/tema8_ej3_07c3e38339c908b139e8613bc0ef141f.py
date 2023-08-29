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
    #número de palabras, el número total de caracteres, el largo promedio de las palabras, el número de espacios, y el número de caracteres de puntuación(que no sean letras o espacios)
    numeroCaracteres = len(frase)

    nuevafrase = frase.strip(".")
    listaPalabras= nuevafrase.split()
    numeroPalabras = len(listaPalabras)

    almacenaLongitudes=0
    for palabra in listaPalabras:
        almacenaLongitudes += len(palabra)
    longitudpromedio= round(almacenaLongitudes/numeroPalabras,2)

    contador = 0
    espacios=0
    while contador < numeroCaracteres:
        if frase[contador] == " ":
            espacios += 1
            contador +=1

        else:
            contador+=1

    puntuacion = 0
    for elemento in frase:
        if elemento in [".",",","-"]:
            puntuacion+=1

    return (numeroPalabras, numeroCaracteres, longitudpromedio, espacios, puntuacion)
    





         