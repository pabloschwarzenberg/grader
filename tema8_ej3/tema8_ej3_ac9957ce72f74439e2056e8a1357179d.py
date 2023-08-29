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
    _alphabet = ['á', 'í', 'ú', 'é', 'ó', 'ñ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    _count_char = ""
    _count_palabras = 0
    _aux_count = 0
    _palabras = []
    _count_espacios = 0
    _whatever = 0
    frase = frase.lower()

    for index, i in enumerate(frase):
        if (frase[index-1] not in _alphabet or index == 0) and frase[index] in _alphabet:
            _comienzo_palabra = _aux_count
            _count_palabras += 1
        elif (frase[index] in _alphabet) and (frase[index+1] not in _alphabet):
            _palabras.append(_aux_count - _comienzo_palabra + 1)
        if i == ' ':
            _count_espacios += 1
        elif i != '\n' and i not in _alphabet:
            _whatever += 1
        _count_char += i
        _aux_count += 1

    _sum = 0

    for n in _palabras:
        _sum += n
    _largo_promedio = _sum / _count_palabras

    return _count_palabras, len(_count_char), _largo_promedio, _count_espacios, _whatever

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         