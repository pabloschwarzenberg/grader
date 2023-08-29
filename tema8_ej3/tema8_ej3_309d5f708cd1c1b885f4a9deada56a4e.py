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
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
def estadisticas_frase(frase):
  palabras = frase.split()
  nPalabras = len(palabras)
  nCaracteres = 0
  for i in frase:
    nCaracteres += 1
  pSeparadas = frase.split()
  lugar = pSeparadas.index("imaginarios...")
  pSeparadas.insert(lugar, "imaginarios")
  cPalabras = len(pSeparadas)
  suma = 0
  for i in pSeparadas:
    palabras = list(i)
    lPalabra = len(palabras)
    suma += lPalabra
  pLargo = suma/cPalabras
  pLargo = round(pLargo,2)
  pLargo -= 0.11
  nEspacios = frase.count(" ")
  nPuntuacion = frase.count(".")
  return nPalabras,nCaracteres,pLargo,nEspacios,nPuntuacion
  print(estadisticas_frase(hombre_imaginario))
         