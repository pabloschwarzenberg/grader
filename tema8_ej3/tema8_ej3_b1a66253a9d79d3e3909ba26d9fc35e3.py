
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
    frase = [str(x) for x in frase]
    palabras = 0
    caracteres = 0
    espacios = []
    promedio = []
    puntuacion = []
    p = 0
    for x,y in enumerate(frase):
        if y != ' ' or y != '\n' or y !='.':
            caracteres += 1
    
    for x,y in enumerate(frase):
        if y == ' ' or y == '\n' or y == '\t':
            if frase[x] == frase[x+1]:
                palabras -=1
            palabras += 1
    
    for x,y in enumerate(frase):
        p +=1
        if y == ' ' or y == '\n' or y == '\t' or y=='.':
            promedio.append(p-1)
            p = 0
        for x,y in enumerate(promedio):
            if y == 0:
                promedio.pop(x)
    for x,y in enumerate(frase):
        if y == ' ':
            espacios.append(x)
        
    for x,y in enumerate(frase):   
        if y == '.':
            puntuacion.append(x)


            
    
 

    w = (sum(promedio)/len(promedio))
    w = round(w,3)


    
    return(palabras,caracteres,w,len(espacios),len(puntuacion))



estadisticas_frase(hombre_imaginario)
         