s = """
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


def estadisticas_frase(s):
    palabras = s.split()
    cantPalabras = len(palabras)
    caracteres = len(s)
    espacios = 0
    for i in range(len(s)):
        if s[i] == " ":
            espacios += 1

    puntos = 0
    contCaracter = 0
    for palabra in palabras:
        for caracter in palabra:
            if caracter != ".":
                contCaracter += 1
            else:
                puntos += 1

    return "(" +str(cantPalabras) + ", " + str(caracteres) + ", " + str(contCaracter / cantPalabras) + ", " + str(
        espacios) + ", " + str(puntos) + ")"


if __name__ == "__main__":
    print(estadisticas_frase(s))
