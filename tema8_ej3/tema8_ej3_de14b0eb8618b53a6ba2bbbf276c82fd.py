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
    cantidadcaracteres=len(frase)
    FS=frase.split()
    cantidadespacios = 0
    cantidadpuntos= 0
    cantidadpalabras = len(FS)
    for i in frase:
        if i==" ":
            cantidadespacios=cantidadespacios+1
    for i in frase:
        if i == ".":
            cantidadpuntos=cantidadpuntos+1
    cantidadletras=0
    nuevafrase=frase.strip(".")
    Listnuevafrase = nuevafrase.split()
    for palabra in Listnuevafrase:
        cantidadletras=cantidadletras+len(palabra)
        
    media= float(cantidadletras) / float(cantidadpalabras)
    
    return cantidadpalabras,cantidadcaracteres,media,cantidadespacios,cantidadpuntos       