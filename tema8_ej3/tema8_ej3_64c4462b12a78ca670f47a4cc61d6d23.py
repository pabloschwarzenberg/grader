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
    frase_t = frase.replace('\n',' ')
    temp = frase_t.strip(' .')
    temp = temp.split(' ')
    if '' in temp:
        for i in range(temp.count('')-1):
            temp.remove('')
    print(temp)
    n_palabras = len(temp)-1
    n_caracteres = len(frase)
    a = 0
    for i in temp:
        for n in i:
            a += 1
    print(a)
    largo_promedio = a / n_palabras
    n_espacios = frase.strip(' \n').count(' ')
    n_puntuacion = n_caracteres - a - n_espacios - frase.count('\n')
    return(n_palabras,n_caracteres,largo_promedio,n_espacios,n_puntuacion)
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         