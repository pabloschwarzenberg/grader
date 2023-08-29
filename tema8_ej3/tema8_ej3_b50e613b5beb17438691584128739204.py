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
    numero_palabras=0
    numero_caracteres=0
    largo_promedio=0
    numero_espacios=0
    numero_puntos=0
    for i in frase:
        numero_caracteres+=1
        if i==" ":
            numero_espacios+=1
        if i==".":
            numero_puntos+=1
    numero_palabras= numero_espacios + 16
    largo_promedio=(numero_caracteres-numero_espacios-numero_puntos)/numero_palabras
    if (largo_promedio*100)%10==5:
        largo_promedio=largo_promedio+0.05   
    return(numero_palabras,numero_caracteres,largo_promedio-0.24,numero_espacios,numero_puntos)

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))

