#Creador: Daniel Ugarte
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
def estadisticas_frase(fra):
    caracteres = len(fra)
    num_espacios  = 0
    num_puntiacion = 0
    j = " "
    for j in fra:
        if j == " ":
            num_espacios = num_espacios + 1
        if j == ".":
            num_puntiacion = num_puntiacion +1
    fra = fra.strip(".")
    pal = len(fra.split())
    
    l_prom = list(fra.split())
    suma = 0
    sum = 0 
    for i in range(pal):
        suma = len(l_prom[i])
        i = i + 1
        sum = sum + suma
    promedio = sum/pal
    return pal, caracteres, promedio, num_espacios, num_puntiacion
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))


         