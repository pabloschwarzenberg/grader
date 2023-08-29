hombre_imaginario = "\n"\
                    "El hombre imaginario\n" \
                    "vive en una mansión imaginaria\n" \
                    "rodeada de árboles imaginarios\n" \
                    "a la orilla de un río imaginario\n" \
                    "\n"\
                    "De los muros que son imaginarios\n" \
                    "penden antiguos cuadros imaginarios\n" \
                    "irreparables grietas imaginarias\n" \
                    "que representan hechos imaginarios\n" \
                    "ocurridos en mundos imaginarios\n" \
                    "en lugares y tiempos imaginarios\n" \
                    "\n"\
                    "Todas las tardes tardes imaginarias\n" \
                    "sube las escaleras imaginarias\n" \
                    "y se asoma al balcón imaginario\n" \
                    "a mirar el paisaje imaginario\n" \
                    "que consiste en un valle imaginario\n" \
                    "circundado de cerros imaginarios..."

#hombre_imaginario = "a la orilla de un río imaginario"
def estadisticas_frase(frase):
    i=0
    palabras=1
    espacios=0
    puntuacion=0
    largo = int(len(frase))

    for i in frase:
        if i == " ":
            espacios+=1
        if i in ".":
            puntuacion+=1
        if i in " " or i in "\n":
            palabras+=1

    promedio= int(largo-espacios-puntuacion)/(palabras)

    return palabras-3, largo, round(promedio,2), espacios, puntuacion
         