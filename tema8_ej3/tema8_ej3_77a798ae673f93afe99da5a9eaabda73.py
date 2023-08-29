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
    puntos=frase.count(".")
    numero=len(frase)
    espacios=frase.count(" ")
    frase=frase.replace("\n\n"," ")
    frase=frase.replace("\n"," ")
    frase=frase.lower()
    frase=frase.replace("á","a")
    frase=frase.replace("é","e")
    frase=frase.replace("í","i")
    frase=frase.replace("ó","o")
    frase=frase.replace("ú","u")
    frase=frase.split(" ")
    espaciosvacios=frase.count(" ")
    numeropalabra=len(frase)-1
    a=0
    for i in frase:
      i=i.replace(".","")
      a=a+len(i)
    prom=round((a/(len(frase)-1)),2)
    print(frase)
    return(numeropalabra,numero,prom,espacios,puntos)

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         