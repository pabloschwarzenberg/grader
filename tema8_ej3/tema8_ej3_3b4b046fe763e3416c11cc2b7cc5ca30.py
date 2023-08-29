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
def estadisticas_frase(a):
    total_palabras=0
    total=0
    largo_palabras=0
    espacios=0
    puntuacion=0
    #PALABRAS
    texto=a.split('\n')
    print(texto)
    for i in texto:
        texto_2=i.split(' ')
        #ESPACIOS
        espacios=espacios+len(texto_2)-1
        print(texto_2)
        if not(texto_2==['']):
            total_palabras=total_palabras+len(texto_2)
            for k in texto_2:
                for j in k:
                    #LARGO PROMEDIO PALABRRAS(SUMA)
                    if not(j==',' or j=='.' or j==';' or j=='¿' or j=='?' or j=='!' or j=='¡'):
                        largo_palabras+=1
                    else:
                        #PUNTUACION
                        puntuacion+=1
    #CARACTERES
    total_caracteres=len(a)
    #LARGO PROMEDIO DE PALABRAS
    largo_palabras=largo_palabras/total_palabras
    return total_palabras,total_caracteres,largo_palabras,espacios,puntuacion
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         