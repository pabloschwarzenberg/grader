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

def estadisticas_frase(string):
    string=list(string)
    # variables
    espacio=[" "]
    salto=["\n"]
    caracter_puntuacion=[",",".",":",";","-","(",")","[","]","{","}","¿","?","«","»",'"',"'",]
    # contadores
    conta_espacio=0
    conta_caracpunt=0
    conta_letras=0
    conta_palabras=0
    prom_l_palabras=0
    total_caracteres=0

    contador_min=0
    contador_max=len(string)
    while contador_min < contador_max:
        if string[contador_min] in espacio:
            conta_espacio+=1
            conta_palabras+=1
        elif string[contador_min] in salto:
            conta_palabras+=1
        elif string[contador_min] in caracter_puntuacion:
            conta_caracpunt+=1
        elif string[contador_min] not in (espacio and caracter_puntuacion):
            conta_letras+=1
        contador_min=contador_min+1
    #para descontar el espacio final e inicial que se agrega a las palabras
    conta_palabras-=2
    prom_l_palabras=conta_letras/conta_palabras
    #se agregan los espacios que se restaron antes
    total_caracteres=(conta_letras+conta_palabras+2+conta_caracpunt)
    """print(f"Total de letras: {conta_letras}")
    print(f"Total de caracteres de puntuación: {conta_caracpunt}")
    print(f"Total de espacios: {conta_espacio}")
    print(f"Total de caracteres: {total_caracteres}")
    print(f"Largo promedio de palabras: {prom_l_palabras}")"""

    return conta_palabras, total_caracteres, prom_l_palabras, conta_espacio, conta_caracpunt

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))

         