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

def estadisticas_frase(s):
    v=len(s)
    l=s.split()
    e=len(l)
    i=0
    cont=0    
    while i< len(s):
        if s[i]==' ' or s[i]=='.' or s[i]=='\n':
            cont=cont+1    
        i=i+1        
        x=len(s)-cont
        y=x/len(l)        
    cont2=0
    j=0
    while j<len(s):    
        if s[j]== ' ':
            cont2=cont2+1
        j=j+1 
    k=0
    cont3=0
    while k<len(s):
        p=s[k]
        if  p=='.':
            cont3=cont3+1
        k=k+1
    return e,v,y,cont2,cont3

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         