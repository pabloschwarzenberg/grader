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
    caracter="\n"
    caracter2="."
    lista=list(frase)
    for caracter in frase:
        frase1=frase.replace("\n"," ")
    for caracter2 in frase:
        frase1=frase1.replace(".","")
    frase1=frase1.split()
    numero_palabras=len(frase1)
    frase1="".join(frase1)
    lista_letras=list(frase1)
    print(lista_letras)
    numero_caracteres=len(lista)
    numero_letras=len(lista_letras)
    lista2=list(frase)
    numero_puntos=lista2.count(".")
    numero_espacios=lista.count(" ")
    promedio_largo=float(numero_letras/numero_palabras)
    
    return(numero_palabras,numero_caracteres,promedio_largo,numero_espacios,numero_puntos)
    
         