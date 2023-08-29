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
    l=list(frase)
    caracteres=len(l)
    espacios=(l.count(" "))
    puntuacion=(l.count(",")+l.count(";")+l.count(".")+l.count(":"))
    lineas=l.count("\n")
    saltos = l.count("\n\n")
    palabras=espacios + lineas -saltos
    nopalabras=espacios+puntuacion
    letras=caracteres-nopalabras
    promedio=letras/palabras
    print("(",palabras,",",caracteres,",",promedio,",",espacios,",",puntuacion,")")
     
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         