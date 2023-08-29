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
    numero_palabras     = 0
    total_caracteres    = 0
    largo_promedio      = 0
    numero_espacios     = 0
    numero_puntuacion   = 0
    extranos            = [",","."," ","\n"]
    caractes            = [",","."]
    espacio             = " "
    contador            = 0
    largos_palabras     = []
    for i in frase:
        if i in extranos:
            if i in caractes:
                numero_puntuacion += 1
            if i == espacio:
                numero_espacios += 1
            if contador != 0:
                largos_palabras.append(contador)
                numero_palabras += 1
                contador = 0
        else:
            contador +=1
        total_caracteres += 1
    acumulador = 0
    for i in largos_palabras:
        acumulador += i
    largo_promedio = round(acumulador/len(largos_palabras),2)
    return numero_palabras,total_caracteres,largo_promedio,numero_espacios,numero_puntuacion
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         