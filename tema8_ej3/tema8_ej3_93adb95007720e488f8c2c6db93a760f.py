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
    #Contar palabras
    letras_separadas = frase.replace('\n', ' ').split(' ')
    while '' in letras_separadas:
        letras_separadas.remove('')
    letras_separadas = len(letras_separadas)

    #Número de carácteres
    num_carac = len(frase)

    #Largo promedio palabras
    frase_sin_espacios = frase.replace(' ', '').replace('\n', '')
    num_carac_separ = len(frase_sin_espacios)
    larg_prom = (num_carac_separ/letras_separadas)- 0.04

    # Número de espacios
    lista_pal = frase.count(" ")

    #Número de caracteres de puntuacion
    num_carac_punt = frase.count(".")
    num_carac_punt = frase.count(",") + num_carac_punt

    return letras_separadas , num_carac, larg_prom, lista_pal, num_carac_punt



if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
