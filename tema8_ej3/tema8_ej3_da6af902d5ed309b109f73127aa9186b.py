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
  espacios=0
  lista=[] 
  largo=len(frase)
  espacios=frase.count(" ")
  puntuacion=frase.count(".")+frase.count(",")+frase.count(";")

  frase = frase.replace("\n"," ")
  variable = frase.split(" ")
  suma=0-puntuacion
  lista=[]
  
  for recorrido in range(len(variable)):
    if variable[recorrido]!="":
      lista.append(variable[recorrido])
      suma += len(variable[recorrido])
  palabras=len(lista)
  promedio=suma/palabras
  final = (palabras,largo,promedio,espacios,puntuacion)
  return final