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
    i=0
    ñ=0
    while i<len(frase):
        if frase[i]==" " or frase[i]=="\n":
            ñ=ñ+1
        if frase[i]=="." or frase[i]==",":
            ñ=ñ-1
        i=i+1
            
    palabra=ñ+1
    caracteres=len(frase)
    l=0
    k=0
    while l<len(frase):
        if frase[l]==" " or frase[l]=="\n" or frase[l]=="." or frase[l]==",":    
            k=k+1
        l=l+1
    f=len(frase)-k           
    promedio=f/palabra
    j=0
    k=0
    while j<len(frase):
        if frase[j]==" ":
            j=j+1
            k=k+1
            
        else:
            j+=1
            espacio=k
    q=0
    i=0
    while i<len(frase):
        if frase[i]=="." or frase[i]==",":
            q+=1
        i+=1
    puntuacion=q
    return(palabra,caracteres,promedio,espacio,puntuacion)
    
    

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         