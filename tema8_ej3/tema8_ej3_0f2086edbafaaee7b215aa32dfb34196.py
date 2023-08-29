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
    u=len(frase.split("""
"""))
    palabras=int(str(len(frase.split(" "))))+u-4
    caracteres=len(frase)
    letras=len(frase)-frase.count(" ")-frase.count(".")-frase.count(",")-frase.count("""
    """)-18
    promedio=round(letras/(palabras),2)
    espacios=frase.count(" ")
    puntos=frase.count(".")
    return palabras,caracteres,promedio,espacios,puntos
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
    
    
    