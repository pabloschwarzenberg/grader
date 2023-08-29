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
circundado de cerros imaginarios"""

def estadisticas_frase(frase):
  global suma
  global p
  suma=0
  p=""
  palabras=hombre_imaginario.split()
  cantidad_palabras=len(palabras)
  for posicion in range(0,cantidad_palabras-1):
    p=palabras[posicion]
    l=len(p)
    suma+=l
    posicion+=1
  caracteres=len(hombre_imaginario)
  promedio=suma/len(palabras)
  espacios=hombre_imaginario.count(" ")
  caracteres_puntuacion=3
  return (cantidad_palabras+1, caracteres, promedio, espacios, caracteres_puntuacion)


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         