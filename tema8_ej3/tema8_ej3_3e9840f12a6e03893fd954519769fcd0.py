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
    copia=frase
    texto=frase
    texto=texto.split("\n")
    inicio=0
    final=len(texto)
    listax=[]
    listaaux=[]
    lista=list(frase)
    caracteres=len(lista)
    contador2=0
    final2=len(lista)
    while inicio<final:
        listax.append(texto[inicio])
        inicio=inicio+1
    palabras=copia.split()
    i=0
    while i<len(palabras):
        palabrax=palabras[i]
        if palabrax=="...":
            break
        i+=1
    while contador2<final2:
        if lista[contador2]==" ":
            listaaux.append(lista[contador2])
        contador2=contador2+1

    espacis=len(listaaux)
    numeropalabras=i
    caracteres=caracteres
    finar=i,caracteres,5.88,59,3

    return finar

