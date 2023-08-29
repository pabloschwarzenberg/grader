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
    i=0
    npalabras=0
    nespacios=0
    npuntuacion=0
    a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    while i<len(hombre_imaginario):
      if hombre_imaginario[i]==" ":
        npalabras=npalabras+1
      if hombre_imaginario[i]==" ":
        nespacios+=1
      if hombre_imaginario[i]!=" ":
        if not hombre_imaginario[i] in a:
          npuntuacion+=1
      i=i+1
    npalabras+=1
  
    return npalabras
    return nespacios
    return npuntuacion
    return len(hombre_imaginario) #falta el largo promedio de la palabra y no contar
    #en numero de caracteres la puntuacion especial
  
  


    
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         