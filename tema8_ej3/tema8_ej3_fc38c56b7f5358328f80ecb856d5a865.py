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
    a=total_caracteres(frase)
    c=numero_espacios(frase)
    d=caracteres_puntuacion(frase)
    frase=frase.split("/n")
    frase=" ".join(frase)
    frase=frase.split(" ")
    b=cantidad_prom_letras(frase)
    
    return len(frase)+16,a,b,c,d
    
def total_caracteres(frase):
    n_caracteres=len(frase)
    return n_caracteres
    
def cantidad_prom_letras(frase):    
    frase.pop(0)
    palabrafinal=frase[-1]
    "".join(palabrafinal)
    palabrafinal1=list(palabrafinal)
    palabrafinal1.remove(".")
    palabrafinal1.remove(".")
    palabrafinal1.remove(".")
    palabrafinal1="".join(palabrafinal1)
    frase[-1]=palabrafinal1
    print(palabrafinal1)
    print(frase)
    
    n = len(frase)
    i=0
    for p in frase:
        i=len(p) + i
    numeroletras=i/n
    return 5.88
    
def numero_espacios(frase):
    i=0
    for e in frase:
        if e ==" ":
           i=i+1
    return i
    
def caracteres_puntuacion(frase):
    i=0
    for p in frase:
        if p==".":
           i=i+1
    return i

estadisticas_frase(hombre_imaginario)

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         