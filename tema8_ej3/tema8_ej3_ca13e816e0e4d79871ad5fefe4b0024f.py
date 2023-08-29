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
  f=frase
  c=0
  e=0
  l=0
  for i in f:
    if i==' ':
      e+=1
    elif (not i.isalpha()) and (i !='\n'):
      c+=1
  pal=f.split()
  h=len(f)
  for i in pal:
    if i.isalpha():
      l+=len(i)
    else:
      l+=len(i.strip('.'))
  l/=len(pal)
  return len(pal), h, l, e, c

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         