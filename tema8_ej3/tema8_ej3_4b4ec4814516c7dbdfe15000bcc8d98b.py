hombre_imaginario = """El hombre imaginario
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

    
    caracteres=len(s)
    


    listapalabras=s.replace(".","")
    listapalabras=listapalabras.split()
    palabras=len(listapalabras)

    espacios=s.count(" ")
    
    comas=s.count(",")
    puntos=s.count(".")
    dospuntos=s.count(":")
    puntocoma=s.count(";")
    puntuacion=comas+puntos+dospuntos+puntocoma


    elementos=s.replace(".","")
    elementos=elementos.split()
    print (elementos)
    print(len(elementos))
    largopalabras=[]
    for i in range(len(elementos)):
        largopalabras.append(len(elementos[i]))
        
    suma=sum(largopalabras)
    print(suma)
    
    promedio=suma/palabras

    
    return palabras,caracteres,promedio,espacios,puntuacion
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         