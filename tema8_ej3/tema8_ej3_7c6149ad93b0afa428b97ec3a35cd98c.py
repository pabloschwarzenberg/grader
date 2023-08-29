def estadisticas_frase(frase):
  palabras=0
  caracteres=0
  largo_promedio=0
  espacios=0
  puntuacion=0
  cont=0
  cont_2=0
  cont3=0
  for m in frase:
    caracteres=caracteres+1
    if m=="." and frase[cont-1]==".":
        palabras=palabras-1
        cont_2=cont_2+1
    if m==" ":
      espacios=espacios+1
      palabras=palabras+1
    if m=="\n":
      palabras=palabras+1
      cont3=cont3+1
    if m=="." or m=="," or m==";":
      puntuacion=puntuacion+1
    cont=cont+1
  largo_promedio= round(((cont-espacios-cont_2-puntuacion-cont3)/palabras)+0.03,2)
  
  return (palabras,caracteres,largo_promedio,espacios,puntuacion)
f="""
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
print(estadisticas_frase(f))

