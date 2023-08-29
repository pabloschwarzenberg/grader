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
def contar_letras (frase):
  letras = 0
  for c in (frase):
    if c.insalpha():
      letras += 1
    else:
      pass

def contar_palabras (frase):
  palabras = frase.splint()
  i=0
  while i < len(palabras):
    palabras=palabras[i]
    if palabras == "fin":
      break
def estadisticas_frase(frase):
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         