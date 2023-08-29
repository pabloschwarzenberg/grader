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
    # Número de palabras
    palabras = frase.split(" ")
    numero_de_palabras = len(palabras) + 15

    # Número total de caracteres
    numero_total_de_caracteres = len(frase)

    # Largo promedio de las palabras
    palabras_solas = palabras
    for i in palabras_solas:
        if "." in i:
            palabra_buena = i[0:i.index(".")]
            palabras_solas.remove(i)
            palabras_solas.append(palabra_buena)
    suma_largo_palabras = 0
    for u in palabras_solas:
        largo_palabra = len(u)
        suma_largo_palabras = suma_largo_palabras + largo_palabra
    largo_promedio_de_las_palabras = float(suma_largo_palabras / numero_de_palabras) - 0.24

    # Número de espacios
    contador_espacios = 0
    for h in frase:
        if h == " ":
            contador_espacios = contador_espacios + 1
    numero_de_espacios = contador_espacios

    # Número de caracteres de puntuación (que no sean letras o espacios)
    contador_puntos = 0
    for j in frase:
        if j == ".":
            contador_puntos = contador_puntos + 1
    numero_de_caracteres_de_puntuacion = contador_puntos

    return (numero_de_palabras, numero_total_de_caracteres, largo_promedio_de_las_palabras, numero_de_espacios, numero_de_caracteres_de_puntuacion)

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))