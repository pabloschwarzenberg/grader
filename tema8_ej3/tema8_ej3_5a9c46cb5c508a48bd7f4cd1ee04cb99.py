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
    listPalabras = frase.split()
    numeroPalabras = len(listPalabras) ###
    numeroCaracteres = 0
    for i in frase:
        numeroCaracteres += 1 ###
    largo = 0
    cantPuntos = 0
    for i in listPalabras:
        x = 0
        puntos = []
        while x < len(i):
            if i[x] == '.' or i[x] == ',':
                puntos.append(str(x))
                cantPuntos += 1 ###
            x += 1
        if '.' in i:
            largo = largo + len(i) - len(puntos)
        else:
            largo = largo + len(i)
    largoPromedio = largo / numeroPalabras ###
    cantEspacios = 0
    for i in frase:
        if i == ' ':
            cantEspacios += 1 ###
    return numeroPalabras,numeroCaracteres,largoPromedio,cantEspacios,cantPuntos
est = estadisticas_frase(hombre_imaginario)
print(est)