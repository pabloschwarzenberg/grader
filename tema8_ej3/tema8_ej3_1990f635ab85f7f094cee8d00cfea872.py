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
    frase = frase.lower()
    simbolos = [".",",",";",":","¡","!","¿","?"]
    letras = ["á","é","í","ó","ú","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    palabras = 0
    caracteres = 0
    largo = 0
    espacios = 0
    puntuacion = 0
    for i in frase:
        if i in letras and frase[puntuacion+1] not in letras:
            palabras += 1
        if i in letras:
            caracteres += 1
        if i in simbolos:
            largo += 1
        if i not in letras and i not in simbolos:
            espacios += 1
        puntuacion += 1
    frase_prima = list(frase)
    dos = len(frase_prima)
    lel = 0
    for a in frase_prima:
        if a == " ":
            lel += 1
    largoo = caracteres / palabras
    return palabras,dos,largoo,lel,largo
if __name__=="__main__":
    print(estadisticas_frase(hombre_imaginario))