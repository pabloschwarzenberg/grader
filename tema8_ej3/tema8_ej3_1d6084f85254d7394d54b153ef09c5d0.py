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
  s=0
  d = 0
  for i in frase.split():
    s = s + len(i.replace(".",""))
    d = d+1
 
  promedio = s / d
  espacios = len(frase.split(" "))-1
  puntuacion = len(frase.split("."))-1
  
  return palabras, caracteres, float("{0:.2f}".format(promedio)), espacios,puntuacion



if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         