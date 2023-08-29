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
    lista = hombre_imaginario.split()
    suma_solo_palabras = 0
    caract_espacio = 0
    caract_puntuacion = 0

    numero_palabras = len(lista)
    total_caracteres =len(hombre_imaginario)

    for i in lista:
        largo_palabra = len(i)
        suma_solo_palabras += largo_palabra
    
    for i in hombre_imaginario:
        for x in i:
            if (x == " "):
                caract_espacio += 1

    for i in hombre_imaginario:
        for x in i:
            if (x == "."):
                caract_puntuacion += 1
    
    promedio_palabras = (suma_solo_palabras - caract_puntuacion) / numero_palabras

    return numero_palabras, total_caracteres, promedio_palabras, caract_espacio, caract_puntuacion

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))