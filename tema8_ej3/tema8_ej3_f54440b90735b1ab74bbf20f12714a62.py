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
    cantidad_palabras = len(frase.split())
    cantidad_caracteres = len(frase)
    lista_aux = frase.split()

    contador = 0 
    especiales = 0
    for a in lista_aux:
        contador += len(a)
        for n in a:
            if n == ".":
                especiales += 1
                contador -= 1
    espacios = 0 
    for a in range(len(frase)):
        if frase[a] == " ":
            espacios += 1
    
    largo_prom = contador / cantidad_palabras
    return cantidad_palabras, cantidad_caracteres, largo_prom, espacios, especiales



if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))         