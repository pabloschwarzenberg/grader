def estadisticas_frase(frase):
    espacios=0
    puntos=0
    for m in frase:
        if m == " ":
            espacios=espacios+1
        if m == "." or m == "," or m == ";":
            puntos=puntos+1
    palabras=espacios+16
    largocaracteres=len(frase)
    promedio_letras=(largocaracteres-espacios-puntos-18)/palabras
    return (palabras,largocaracteres,promedio_letras,espacios,puntos)


         
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