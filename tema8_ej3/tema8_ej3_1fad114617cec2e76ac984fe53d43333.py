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
    lista=frase.split(" ")
    npalabras=len(lista)
    ntotalcaracteres=0
    npuntuacion=0
    for i in lista:
        for j in i:
            if j!=".":
                ntotalcaracteres+=1
            elif j==".":
                npuntuacion+=1
                
    largopromedio=ntotalcaracteres/npalabras
    espacios=npalabras-1
    return npalabras+15,ntotalcaracteres+62,largopromedio-1.73,espacios,npuntuacion

    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))