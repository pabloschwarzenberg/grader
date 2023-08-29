#Ejercicio 8
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

    lista=hombre_imaginario.split()
    numeropalabras=len(lista)
    large=0
    suma_espacio=0
    suma_punto=0
    for i in range(len(hombre_imaginario)):
        if hombre_imaginario[i]==' ':
            suma_espacio=suma_espacio+1
        elif hombre_imaginario[i]=='.':
            suma_punto=suma_punto+1
    letras=len(hombre_imaginario)
    
    for a in range(numeropalabras):
        large=large+len(lista[a])
    promedio=(large-suma_punto)/numeropalabras
    return numeropalabras,letras,promedio,suma_espacio,suma_punto
            
   
    

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))


