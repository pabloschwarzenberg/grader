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
def estadisticas_frase(s):
    cont_caracteres=0
    cont_palabras=1 
    cont_espacios=0
    puntuacion=0
    letras="abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for letra in s:
        if letra in letras:
            cont_caracteres+=1
        elif letra==" ":
            cont_espacios+=1
            cont_palabras+=1
        else:
            puntuacion+=1
    largoprom=(cont_caracteres-puntuacion)//cont_palabras

    return cont_palabras,cont_caracteres,largoprom,cont_espacios,puntuacion
    pass
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
    

         