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
    import string
    palabras = frase.split()
    n_palabras = len(palabras)
    c_tot = sum(len(palabra) for palabra in palabras) + frase.count(' ') + frase.count('\n')
    c_sin_p = sum(len(palabra.strip(string.punctuation)) for palabra in palabras)

    len_prom = c_sin_p / n_palabras

    n_esp = frase.count(' ')
    n_p = sum(caracter in string.punctuation for caracter in frase)
    return n_palabras, c_tot, len_prom, n_esp, n_p

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         