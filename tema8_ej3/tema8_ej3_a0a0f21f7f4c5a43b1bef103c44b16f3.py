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
    lista = frase.split()
    cont_palabras = 0
    for i in lista:
        cont_palabras+=1

    cont_caracteres = 0
    for i in frase:
        cont_caracteres+= 1
    nuevo_texto = ""
    for i in hombre_imaginario:
        if i == ".":
            break
        else:
            nuevo_texto += i
    nuevo_texto = nuevo_texto.split()
    lista_largo = []
    for x in nuevo_texto:
        lista_largo.append(len(x))
    
    promedio = sum(lista_largo)/len(lista_largo)

    cont_espacios = 0
    cont_puntuacion = 0
    for i in hombre_imaginario:
        if i == " ":
            cont_espacios += 1
        if i == ".":
            cont_puntuacion += 1
    total = (cont_palabras,cont_caracteres,promedio,cont_espacios,cont_puntuacion)
    return total