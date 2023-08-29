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
    lista_palabras=frase.split(" ")
    a=len(lista_palabras)
    b=len(frase)
    c=frase.count(" ")
    d=frase.count(",")
    e=frase.count(".")
    f=frase.count(";")
    g=frase.count(":")
    h=d+e+f+g
    l=0
    for i in range(a):
        l=l+len(lista_palabras[i])
    k=l/a
        
        
    return a,b,k,c,h

    
    

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
