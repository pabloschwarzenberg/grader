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
    frase1="".join(frase.splitlines(True))
    print(frase1)
    palabras=0
    caracteres=0
    espacios=0
    caracteres_puntuacion=0
    x=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    largo=len(frase1)
    print("largo:",largo)
    a=list(frase1)
    for i in range(0,largo):
      if a[i]==".":
          caracteres_puntuacion+=1
      elif a[i]==" ":
        espacios+=1
    cosas=caracteres_puntuacion+espacios
    print("cosas",cosas)
    caracteres=largo
    caracteres_alfabeto=largo-cosas-18
    cantidad_palabras=espacios+1+15
    promedio_palabras=caracteres_alfabeto/cantidad_palabras
    
    return (cantidad_palabras,caracteres, promedio_palabras, espacios, caracteres_puntuacion)







if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         