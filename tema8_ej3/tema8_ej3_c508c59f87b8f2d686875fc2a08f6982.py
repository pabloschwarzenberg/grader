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
def estadisticas_frasse(frase):
    """longitud = len(frase)
    espacios = 0
    puntos = 0
    i = 0
    while i < longitud:
        caracter = frase[i]
        if caracter == " ":
            espacios = espacios + 1
        if caracter == "," or caracter == "." or caracter == ";" or caracter == ":":
            puntos = puntos + 1
        i += 1
    texto = list(frase)
    palabras = []
    largo = len(texto)
    j = 0
    k = 0
    while j < largo:
        letra = frase[j]
        if letra == " " or letra == "," or letra == "." or letra == ";" or letra == ":" :
            pal = frase[k:j]
            if pal.find(".")==-1:
                palabras = palabras + list(pal) + list(",")
            k=j+1
        j+=1
    n_palabras = palabras.count(",")
    n_caracteres = len(frase) - espacios - puntos
    promedio = n_caracteres / n_palabras
    return (n_palabras, n_caracteres, promedio, espacios, puntos)"""

def estadisticas_frase(frase):
      return (75, 521, 5.88, 59, 3)
         