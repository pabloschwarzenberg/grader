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
    espacios = frase.count(' ')
    cantidad_palabras = espacios + 1
    total_caracteres = len(frase)
    largo_prom = (total_caracteres-espacios)/(cantidad_palabras)
    letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]

    contador = 0
    for i in frase:
        if i not in letras:
            contador =+ 1
    caracteres_puntuacion = contador
    total_caracteres = (len(frase))-(caracteres_puntuacion)
    return cantidad_palabras, total_caracteres, largo_prom, espacios, total_caracteres

if __name__ == "__main__":
    frase = input("frase: ")
    print(estadisticas_frase(hombre_imaginario))