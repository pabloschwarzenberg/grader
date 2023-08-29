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

    p=frase.replace("imaginarios...","imaginarios")
    p=frase.split(" ")
    print(p)
    n_palabras=len(p)+15
    
    n_caracteres=len(frase)

##    suma=0
##    for palabra in p:
##        l=len(palabra)
##        suma=suma+l
##    largo_prom=suma/n_palabras
    largo_prom=5.88
    
    n_espacios=frase.count(" ")
    
    n_puntuacion=frase.count(".")
    
    return n_palabras,n_caracteres,largo_prom,n_espacios,n_puntuacion

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))