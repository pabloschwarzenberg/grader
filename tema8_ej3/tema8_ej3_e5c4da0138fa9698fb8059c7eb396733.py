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
    palabras = len(frase.split())
    caracteres = len(frase)
    largoPromedio = 0
    listaPalabras = frase.split()
    puntuaciones = 0
    for palabra in listaPalabras:
      tam = len(palabra.strip(".,\n"))
      for caracter in palabra:
        if caracter in ".,;":
          puntuaciones+=1
      largoPromedio += tam
    largoPromedio /= palabras
    espacios = frase.count(" ")
    return palabras, caracteres, largoPromedio, espacios, puntuaciones

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         