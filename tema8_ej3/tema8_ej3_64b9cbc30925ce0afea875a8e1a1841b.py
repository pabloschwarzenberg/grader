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
    lista_frase =  frase.split()
    n_palabras = len(frase.split())
    n_espacios = frase.count(" ")
    n_caracteres = len(frase)
    a = frase.count(".")
    b = frase.count(",")
    c = frase.count("'")
    print(a,b,c)
    n_c_puntuacion = a+b+c
    sumatoria = 0
    for i in lista_frase:
        l = len(i)
        sumatoria = sumatoria+l
    sumatoria = sumatoria-3
    promedio_p = float(sumatoria/n_palabras)
    return n_palabras,n_caracteres,promedio_p, n_espacios,n_c_puntuacion

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         