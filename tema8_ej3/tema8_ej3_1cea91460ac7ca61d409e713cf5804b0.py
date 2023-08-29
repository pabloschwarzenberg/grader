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
    cantidad_caracteres=len(frase)
    cantidad_palabras=len(frase.split())
    i=0
    largos=0
    while i<cantidad_palabras:
        largos+=len(frase.split()[i])
        i+=1
    promedio=(largos-3)/cantidad_palabras
    espacios=frase.count(" ")
    especiales=0
    for e in frase:
        if 64<ord(e)<91 or 96<ord(e)<123 or ord(e)==32 or ord(e)==10 or ord(e)>126:
            especiales+=0
        else:
            especiales+=1
    return cantidad_palabras,cantidad_caracteres,promedio,espacios,especiales


