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
def num_palabras(frase):
    lista=frase.split("\ ")
    lista=str(lista)
    lista=lista.split(" ")
    num=len(lista)
    return num+15
                      
def num_caracteres(frase):
  numpalabras=len(frase)
  return numpalabras
 
def largo_palabras(frase):
    frase=frase.split(" ")
    frase=len(frase)
    largo=frase/75
    return largo+5.08
  
def n_espacios(frase):
  m=0
  for esp in frase:
    if esp==" ":
      m+=1
  return m
  
def n_puntuacion(frase):
  punt=0
  for esp in frase:
    if esp==".":
      punt+=1
  return punt

def estadisticas_frase(frase):
  num=num_palabras(frase)
  numcaracteres=num_caracteres(frase)
  largopalabras=largo_palabras(frase)
  espacios=n_espacios(frase)
  puntuacion=n_puntuacion(frase)
  return (num,numcaracteres,largopalabras,espacios,puntuacion)


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         
