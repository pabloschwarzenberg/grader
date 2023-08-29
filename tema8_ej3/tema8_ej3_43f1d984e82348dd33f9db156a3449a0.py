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
    numero_espacios=frase.count(" ")
    a=frase
    while """
""" in a:
        b=a.index("""
""")
        l=list(a)
        l[b]=" "
        a="".join(l)
    z=list(a)
    while "." in z:
        z.remove(".")
    while "," in z:
        z.remove(",")
    while ";" in z:
        z.remove(";")
    while ":" in z:
        z.remove(":")
    x="".join(z)
    X=x.split(" ")
    while "" in X:
        X.remove("")
    numero_palabras=len(X)
    numero_caracteres=len(frase)
    e=0
    g=[]
    while e<len(X):
        f=len(X[e])
        g.append(f)
        e+=1
    h=sum(g)
    promedio_palabras=h/numero_palabras
    numero_caracteres_puntuacion=frase.count(".")+frase.count(",")+frase.count(";")+frase.count(":")
    return numero_palabras,numero_caracteres,promedio_palabras,numero_espacios,numero_caracteres_puntuacion


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         