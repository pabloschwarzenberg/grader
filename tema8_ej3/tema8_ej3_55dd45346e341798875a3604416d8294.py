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
  sum = 0
  cantidad_puntuacion = 0
  palabras = frase.split()
  cantidad_palabras = len(palabras)
  cantidad_caracteres = len(frase)
  for palabra in palabras:
    for caracter in palabra:
      if caracter.isalpha():
        sum += len(caracter)
      else:
        cantidad_puntuacion += 1
  largo_promedio = sum / len(palabras)
  return cantidad_palabras,cantidad_caracteres,largo_promedio,frase.count(" "),cantidad_puntuacion


if __name__ == "__main__":
  print(estadisticas_frase(hombre_imaginario))