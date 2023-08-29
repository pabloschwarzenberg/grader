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
    palabras = frase.strip().split(" ")
    caract = 0
    for palabra in palabras:
        caract += len(palabra)+1
    letras_tot = 0
    for palabra in palabras:
        letras_tot += len(palabra)
    largo_prom = round(letras_tot/len(palabras),1)
    esp = len(palabras)-1
    puntuacion = frase.count(",") + frase.count(".")
    return len(palabras), caract, largo_prom, esp, puntuacion
 
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))