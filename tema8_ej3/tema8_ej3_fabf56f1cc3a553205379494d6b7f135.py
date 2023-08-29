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
    j=int(frase.count(".")+frase.count(","))
    frase_=list(frase)
    m=int(len(frase))
    q=int(frase.count("""
""")-3)
    u=int(frase.count(" "))
    p=int(m-q-3-u-j)
    palabras=int(u+1+q)
    promedio_palabras=float(p/palabras)
    return (palabras,m,promedio_palabras,u,j)
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         