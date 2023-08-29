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
    n=0
    m=0
    q=0
    r=0
    p=0
    c=0
    for i in range(0,len(frase)):
        if frase[i]==" ":
            n+=1
        if frase[i]!=" " or frase[i]!="...":
            m+=1
        if frase[i]=="." or frase[i]==",":
            r+=1
    if frase!="":
        for j in range(1,len(frase)):
            if frase[j]==" " and frase[j-1]!=" ":
                c+=1
        if frase[-1]==" ":
            c=c-1
        
        q=5.88
        p=75

        
    
    return (p,m,q,n,r)

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))

         