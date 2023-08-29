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
    total_caracteres=0
    for k in frase:
        total_caracteres+=1
        
    frase_separada=frase.splitlines()
    palabras=0
    
    largo_total=0
    puntuacion=0
    espacios=0
    for i in frase_separada:
        frase=i.split(" ")
        espacios+=len(frase)-1
        for j in frase:
            if j != "":
                palabras+=1
                for k in j:
                    
                    if k != ".":
                        largo_total+=1
                        
                    else:
                        puntuacion+=1
                          
    promedio=largo_total/palabras
    
    return palabras,total_caracteres,promedio,espacios,puntuacion
    
    


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))

