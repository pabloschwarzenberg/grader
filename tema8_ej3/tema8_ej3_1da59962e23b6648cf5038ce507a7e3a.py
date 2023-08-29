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
    palabras=frase.split()
    x=0
    espacio=0
    puntuacion=0
    totalLargo=0
    correccion=0
    Tcarac=len(frase)
    while x<len(palabras):
        palabra=palabras[x]
        for i in palabra:
            if i == " " or i =="." or i=="," or i==";" or i==":" or i=="(" or i==")" or i=="¿" or i=="?" or i=="-":
                correccion=correccion+1
                pass
            else:
                totalLargo=totalLargo+len(i)
        if palabra=='Fin':
            break
        x=x+1
    for k in frase:
        if k==" ":
            espacio=espacio+1
        elif k=="." or k=="," or k==";" or k==":" or k=="(" or k==")" or k=="¿" or k=="?" or k=="-":
            puntuacion=puntuacion+1
    promedio=totalLargo/x
    return (x, Tcarac, promedio, espacio, puntuacion)
print(estadisticas_frase(hombre_imaginario))