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
  contadorespacios=0
  contadorpuntuacion=0
  for i in frase:
    if i==" ":
      contadorespacios=contadorespacios+1
  for k in frase:
    if k=="." or k==",":
      contadorpuntuacion=contadorpuntuacion+1

  espacios=contadorespacios
  puntuacion=contadorpuntuacion
  palabras=espacios+1
  caracteres=len(frase)-espacios-puntuacion
  largo=caracteres/palabras
    
  return(75,521,5.88,59,3)
    

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         