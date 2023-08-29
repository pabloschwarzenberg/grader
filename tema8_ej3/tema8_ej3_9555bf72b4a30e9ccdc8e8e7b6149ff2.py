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
  abecedario="qwertyuiopasdfghjklñzxcvbnm"
  linea=hombre_imaginario.strip(".").split("""
""")
  linea=list(filter(None, linea))
  palabras=[]
  for i in range(len(linea)):
      linea[i]=str(linea[i]).split(" ")
      for k in range(len(linea[i])):
          palabras.append(linea[i][k])
  npalabras=len(palabras)
  ncaracteres=len(hombre_imaginario)
  xpalabras=0
  for i in range(len(palabras)):
    xpalabras+=len(palabras[i])
  xpalabras/=len(palabras)
  espacios=hombre_imaginario.count(" ")
  puntuacion=hombre_imaginario.count(".")
  return npalabras,ncaracteres,xpalabras,espacios,puntuacion
  pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         