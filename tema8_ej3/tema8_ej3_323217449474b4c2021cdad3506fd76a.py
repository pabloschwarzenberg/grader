hombre_imaginario= """
El hombre imaginario
vive en una mansion imaginaria
rodeada de arboles imaginarios
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
    espacios=0
    for bb in frase:
        if (bb==" "):
            espacios=espacios+1
    frase=frase.replace("\n"," ")
    w=frase.split(" ")
    cont=0
    for val in w:
        if (val==""):
            del w[cont]
        cont=cont+1
    numPalabras=len(w)+1
    caracteres=0
    suma=0
    let=0
    for ii in w:
        tmpcont=0
        for jj in ii:
            let=let+1
            if ((jj>="A" and jj<="Z")or(jj>="a" and jj<="z") or (jj>="Á" and jj<="Ú") or (jj>="á" and jj<="ú")):
                tmpcont=tmpcont+1
                caracteres=caracteres+1
        suma=suma+tmpcont
    promedio=suma/numPalabras
    caracterespunt=0
    for mm in w:
        for nn in mm:
            if not(((nn>="A" and nn<="Z")or(nn>="a" and nn<="z") or (nn>="Á" and nn<="Ú") or (nn>="á" and nn<="ú")or(nn==" "))):
                caracterespunt=caracterespunt+1
    return numPalabras, caracteres, promedio, espacios, caracterespunt
    
if __name__=="__main__":
    print(estadisticas_frase(hombre_imaginario))
