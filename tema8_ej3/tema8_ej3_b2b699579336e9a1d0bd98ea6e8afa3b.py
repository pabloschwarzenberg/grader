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

def estadisticas_frase(mensaje):
  largo_caract=len(mensaje)
  espacio=0
  puntos=0
  for l in mensaje:
      if l==" ":
        espacio=espacio+1
      elif l==".":
        puntos=puntos+1

  mens_aux=mensaje.replace("\n"," ")
  mens_corr=mens_aux[1:(len(mensaje)-3)]
  print(mens_corr)

  frases=mens_corr.split(" ")
  print(frases)
  cantidad_frases=len(frases)-2
  largo_palabras=[]
  suma_largos=0
  for i in frases:
    largo_palabras.append(len(i))
  for j in largo_palabras:
    suma_largos=suma_largos+j
  promedio_largo=suma_largos/(cantidad_frases)

  return(cantidad_frases, largo_caract, promedio_largo, espacio, puntos)
  

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         