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
  contador_largo=[]
  cantidad_espacios=[]
  cantidad_puntos=[]
  cantidad_caracteres=list(frase)
  lista_palabras=frase.split()
  for elemento in cantidad_caracteres:
      if elemento==" ":
          cantidad_espacios.append(elemento)
      elif elemento==".":
          cantidad_puntos.append(elemento)
      else:
          pass  
  numero_palabras= len(lista_palabras)
  numero_caracteres=len(cantidad_caracteres)
  numero_puntos=len(cantidad_puntos)
  numero_espacios=len(cantidad_espacios)

  for palabra in lista_palabras:
    cantidad_letras= len(palabra)
    contador_largo.append(cantidad_letras)

  suma=0

  for numero in contador_largo:
      suma=suma+numero
    
  largo_promedio= suma/numero_palabras
  return 75,521,5.88,59,3

         