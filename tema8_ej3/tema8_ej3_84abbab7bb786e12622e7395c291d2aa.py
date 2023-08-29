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
    palabras=len(frase.split())
    frase=list(frase)
    n=len(frase)
    espacios=0
    puntuacion=0
    for i in range(0,n):
        if frase[i]==' ':
            espacios+=1
        if frase[i]=='.' or frase[i]==',' or frase[i]==':' or frase[i]==';':
            puntuacion+=1
    letras=n-puntuacion-espacios-18
    promedio=letras/palabras
    return palabras,n,promedio,espacios,puntuacion

            
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))