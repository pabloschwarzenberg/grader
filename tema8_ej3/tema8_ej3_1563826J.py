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
    largo_promedio=0
    numero_de_espacios=list(frase).count(' ')
    list_frase=frase.split(' ')
    numero_de_palabras=len(list_frase)
    numero_de_caracteres=len(frase)
    for a in list_frase:
        largo_promedio+=len(a)
    largo_promedio=largo_promedio/numero_de_palabras
    numero_carac_puntuacion=list(frase).count('.')+list(frase).count(',')+list(frase).count(';')+list(frase).count(':')
        
    
    return numero_de_palabras,numero_de_caracteres,largo_promedio,numero_de_espacios,numero_carac_puntuacion




if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         