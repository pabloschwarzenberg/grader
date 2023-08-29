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
    c=0
    while i<len(frase):
       if frase[i]==" " or frase[i]=="\n":
          c=c+1
       if frase[i]=="." or frase[i]==",":
          c=c-1
       i=i+1
    g=c+1

    j=len(frase)

    i=0
    d=0
    while i<len(frase):
       if frase[i]==" " or frase[i]=="." or frase[i]=="," or frase[i]=="\n":
          d=d+1
       i=i+1

    k=len(frase)-d
   
    
    
       
    e=k/g
    
    i=0    
    f=0
    while i<len(frase):
       if frase[i]==" ":
          f=f+1
       i=i+1
    x=f
    
    i=0
    h=0
    while i<len(frase):
       if frase[i]=="." or frase[i]==",":
         h=h+1
       i=i+1
    z=h
    
    
    return (g,j,e,x,z)
    

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         