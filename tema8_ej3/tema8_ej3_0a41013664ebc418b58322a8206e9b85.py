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
    nueva = frase.replace(" ...","")
    nueva = nueva.split(" ")
    letras = 0
    for palabra in nueva:
        letras = letras + len(palabra)
    print("Número de palabras: ",len(nueva)," Número de caracteres: ",letras," Largo promedio:", letras/len(nueva))
    return

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         