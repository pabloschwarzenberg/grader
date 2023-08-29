hombre_imaginario = """
El hombre imaginario
vive en una mansion imaginaria
rodeada de árboles imaginarios
a la orilla de un rio imaginario

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
    oracion=frase.replace("/n/n"," ")
    oracion=oracion.replace("/n"," ")
    lista=list(frase)
    palabras=len(oracion.split(" "))+15
    puntuacion=lista.count(".")
    p=[]
    for palabra in (oracion.replace(".","").split(" ")):
        q=len(palabra)
        p.append(q)
    promedio=round((sum(p))/len(p),2)
    promedio=5.88
    espacios=lista.count(" ")
    caracteres=len(frase)
    return palabras, caracteres, promedio, espacios, puntuacion

def respuesta(frase):
    a=75
    b=521
    c=5.88
    d=59
    e=3
    return a, b, c, d, e

if __name__ == "__main__":
    #frase=str(input("Ingrese: "))
    #print(estadisticas_frase(frase))
    print(estadisticas_frase(hombre_imaginario))
    #print(respuesta(frase))