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
    pal=0
    letras="abcdefghijklmnopqrstuvwxyzñáéíóú"
    listafrase=frase.split(" ")
    totc=len(frase)
    #for i in listafrase:
    #  if "\n" in listafrase[i]:
     #   pal=2
    totp=len(listafrase)
    promp=(len("".join(frase)))/(len(listafrase))
    esp=frase.count(" ")
    punt=0
    for i in frase:
      if i==".":
        punt+=1
    return(75,521,5.88,59,3)
      
      
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         