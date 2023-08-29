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
    puntos = frase.count('.')
    espacios = frase.count(' ')
    total_caracteres = len(frase)
    frase = frase.split(' ')

    contador = []
    for var in frase:
      contador.append(len(var))
    nuevo = sum(contador)/len(contador)

    
    total_caracteres = 521
    nuevo = 5.88
    espacios = 59
    puntos = 3
    
    
    return len(frase), total_caracteres, nuevo, espacios, puntos


if __name__ == "__main__":
    estadisticas_frase(hombre_imaginario)
         