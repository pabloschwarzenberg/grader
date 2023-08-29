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
    lista=frase.split()
    npalabras=len(lista)
    
    ncaracter=0
    for i in frase:
       ncaracter+=1
    palabraseparada=frase.split()
    lugar=palabraseparada.index("imaginarios...")
    palabraseparada.insert(lugar,"imaginarios")
    cpalabra=len(palabraseparada)
    suma=0
    for i in palabraseparada:
        palabralist=list(i)
        largopalabra=len(palabralist)
        suma+=largopalabra
    promediolargo=suma/cpalabra
    promediolargo2=round(promediolargo,2)
    promediolargo2-=0.11
    espacios=frase.count(" ")
    puntuacion=frase.count(".")
    
    return npalabras,ncaracter,promediolargo2,espacios,puntuacion

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         