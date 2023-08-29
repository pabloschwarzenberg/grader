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
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    espacio = " "
    cuenta_letras = 0
    cuenta_espacios = 0
    cuenta_palabras = 0
    frase_separada = frase.split()
    for i in frase_separada:
        cuenta_palabras += 1
    for i in frase:
        if i in letras:
            cuenta_letras += 1
        if i in espacio:
            cuenta_espacios += 1
    return(cuenta_letras,cuenta_espacios, cuenta_palabras)

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         