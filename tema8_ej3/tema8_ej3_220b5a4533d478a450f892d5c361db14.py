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
    x = frase.split()
    can_palab = len(x)   
    fraselista = list(frase)
    num_caract = len(fraselista)
    split = frase.split()
    lista = []
    for i in range(0, len(split)):
        lista.append(len(split[i]))
    x = len(lista)
    lista[x - 1] = 11
    suma = 0
    for i in lista:
        suma += i
    prom_largo = suma / len(lista)
    esp_total = 0
    for i in frase:
        if i == " ":
            esp_total += 1
    pt_total= 0
    for i in frase:
        if i == ".":
            pt_total += 1
    return can_palab, num_caract, prom_largo, esp_total, pt_total