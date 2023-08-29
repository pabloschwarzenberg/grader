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
    import re
    palabras=frase.split(' ')
    fraseNoEspacio= re.sub(r"\s+", "", frase, flags=re.UNICODE).replace(".","")
    palabras2=frase.split()
    nroPalabras=len(palabras2)
    espacios=len(palabras)-1
    totalCaracteres=0
    signosPuntuacion=0
    for m in palabras:
        totalCaracteres=len(frase)
        for l in range(0,len(m)):
            if m[l] == "." or m[l] == "," or m[l] == ";" or m[l] == ":":
                signosPuntuacion+=1
    largoPromedio=len(fraseNoEspacio)/nroPalabras
    return nroPalabras,totalCaracteres,largoPromedio,espacios,signosPuntuacion
         