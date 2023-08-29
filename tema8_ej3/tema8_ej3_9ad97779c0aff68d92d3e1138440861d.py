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

def estadisticas_frase(hombre_imaginario):
    m=0
    n=0
    while m<len(hombre_imaginario):
        if hombre_imaginario[m]==" " or hombre_imaginario[m]=="\n":
            n=n+1
        if hombre_imaginario[m]=="." or hombre_imaginario[m]==",":
            n=n-1
        m=m+1
    numero_palabras=n+1

    lista=list(hombre_imaginario)

    caracteres_totales=len(lista)
    
    m=hombre_imaginario.split(" ")
    numero_espacios=hombre_imaginario.count(" ")
  

    caracteres_especiales_punto=hombre_imaginario.count(".")
    caracteres_especiales_coma=hombre_imaginario.count(",")
    caracteres_especiales_enters=hombre_imaginario.count("\n")
    caracteres_especiales=(caracteres_especiales_punto)+(caracteres_especiales_coma)+(numero_espacios)+(caracteres_especiales_enters)
    

    caracteres_totales2=caracteres_totales-caracteres_especiales
    promedio_palabras=caracteres_totales2/numero_palabras

    return (numero_palabras,caracteres_totales,promedio_palabras,numero_espacios,(caracteres_especiales_punto)+(caracteres_especiales_coma))

    

