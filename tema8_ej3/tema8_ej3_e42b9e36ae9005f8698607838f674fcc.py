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
    caracteres_palabra = 'abcçdefghijklmnñopqrstuvwxyz0123456789áéíóú'
    palabras = []
    nueva_palabra = True
    n_palabra = 0
    espacios = 0
    puntuacion = 0
    x = 0
    while x < len(frase):
        i = frase[x]
        if caracteres_palabra.find(i.lower()) != -1:
            if nueva_palabra:
                n_palabra = len(palabras)
                palabras.append('')
                nueva_palabra = False
            palabras[n_palabra] += i
        elif x != 0:
            nueva_palabra = True
        if i == ' ':
            espacios += 1
        if i == '.' or i == ',' or i == ':' or i == ';':
            puntuacion += 1
        x += 1
    media_len = 0
    for i in palabras:
        media_len += len(i)
    media_len = media_len / len(palabras)
    return len(palabras), len(frase), media_len, espacios, puntuacion


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
