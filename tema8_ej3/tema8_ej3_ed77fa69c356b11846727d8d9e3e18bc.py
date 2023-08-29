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
    contador1 = 0
    #contador1 contara los espacios
    contador2 = 0
    #contador2 contara los signos de puntuación
    contador3 = 0
    frasereal = frase.lower()
    for n in frasereal:
        if  n == """
""":
            contador1 = contador1 + 1

        elif n == " ":

            contador3 = contador3 + 1

        elif n == "." or n == "," or n == "-" or n == ";" or n == ":":
            contador2 = contador2 + 1

        else:
            continue

        
    frase1 = frasereal.replace("."," ")
    frase2 = frase1.replace(","," ")
    frase3 = frase2.replace("-"," ")
    frase4 = frase3.replace(";"," ")
    frase5 = frase4.replace(":"," ")
    frase6 = frase5.replace("á","a")
    frase7 = frase6.replace("é","e")
    frase8 = frase7.replace("í","i")
    frase9 = frase8.replace("ó","o")
    frase10 = frase9.replace("ú","u")
    frase11 = frase10.replace(" ","")
    frase12 = frase11.replace("""
""","")
    caracteres = len(frase10)
    palabras = -2+(contador1+contador3)
    promedio = float(len(frase12)/palabras)

    return palabras,caracteres,promedio,contador3,contador2
        
        
  
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))



if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         