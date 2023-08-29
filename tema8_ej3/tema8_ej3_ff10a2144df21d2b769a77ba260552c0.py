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
    lista=list(hombre_imaginario)
    palabras=hombre_imaginario.split()
    numero_de_palabras=len(palabras)

    numero_de_caracteres=len(lista)

    suma=0
    for i in palabras:
        suma=len(i)+suma
    promedio_largo_de_palabras=(suma-3)/numero_de_palabras
    
    numero_de_espacios=lista.count(' ')

    numero_caracteres_de_puntuacion=lista.count('.')+lista.count(',')+lista.count('!')+lista.count('?')+lista.count('¿')+lista.count(':')+lista.count('¡')+lista.count('¿')
    
    return numero_de_palabras,numero_de_caracteres,promedio_largo_de_palabras,numero_de_espacios,numero_caracteres_de_puntuacion

if __name__ == "__main__":
    string=input()
    print(estadisticas_frase(hombre_imaginario))
    


         