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
    caracteres = len(frase)
    num_esp  = 0
    num_punt = 0
    j = " "
    for j in frase:
        if j == " ":
            num_esp = num_esp + 1
        if j == ".":
            num_punt = num_punt +1
    frase = frase.strip(".")
    palabras = len(frase.split())
    
    l_prom = list(frase.split())
    sumatoria = 0
    suma = 0 
    for i in range(palabras):
        sumatoria = len(l_prom[i])
        i = i + 1
        suma = suma + sumatoria
    promedio = suma/palabras
    return palabras, caracteres, promedio, num_esp, num_punt
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))

