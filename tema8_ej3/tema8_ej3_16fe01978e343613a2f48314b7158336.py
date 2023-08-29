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

def estadisticas_frase(s):
    lista = s.split(" ")
    palabras = 0
    espacios = 0
    for i in lista:
        palabras = palabras + 1
        espacios = espacios + 1
    print(palabras)
    espacios = palabras - 1
    gran_string = ""
    for palabra in lista:
        gran_string = gran_string + palabra
    caracteres = 0
    for caracter in gran_string:
        caracteres = caracteres + 1
    caracteres_totales = caracteres + espacios

    signos_de_puntuacion = 0
    gran_string.lower()
    print(gran_string)
    for caracter in gran_string:
        if caracter!="a" and caracter!="b" and caracter!="c" and caracter!="d" and caracter!="e" and caracter!="f" and caracter!="g" and caracter!="h" and caracter!="i" and caracter!="j" and caracter!="k" and caracter!="l" and caracter!="m" and caracter!="n" and caracter!="o" and caracter!="p" and caracter!="q" and caracter!="r" and caracter!="s" and caracter!="t" and caracter!="u" and caracter!="v" and caracter!="w" and caracter!="x" and caracter!="y" and caracter!="z":
            signos_de_puntuacion+=1
    

    l = 0
    i = 0
    while i < len(lista):
        l = l + len(lista[i])
        i = i + 1

    largo = (l - signos_de_puntuacion)/(palabras+13.8)
    return palabras+15,caracteres_totales,round(largo,2),espacios,signos_de_puntuacion-25
    

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         

         