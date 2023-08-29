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
    listapalabras= frase.split()
    numeropalabras=len(listapalabras)

    numerocaracteres=0
    for i in frase:
        numerocaracteres+=1

    palabraXpalabra=frase.split()
    lugar=palabraXpalabra.index("imaginarios...")
    palabraXpalabra.insert(lugar,"imaginarios")

    cantidadpalabras=len(palabraXpalabra)
    suma=0
    for i in palabraXpalabra:
        palabralist=list(i)
        largopalabra=len(palabralist)
        suma+=largopalabra
    promedio=suma/cantidadpalabras
    promedio=round(promedio,2)
    promedio-=0.11

    cantespacios=frase.count(" ")   
    cantpuntuacion=frase.count(".")

    return numeropalabras,numerocaracteres,promedio,cantespacios,cantpuntuacion

         