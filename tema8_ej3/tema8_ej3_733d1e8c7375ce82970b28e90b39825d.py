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
    #quitar \n de la frase
    lista=frase.split("\n")
    Frase=(" ".join(lista))
    caracteres=list(Frase)
    Caracteres=len(caracteres)
    letras=0
    palabras=0
    puntuacion=0
    espacios=0
    L_sinPuntos=[]
    for i in caracteres:
        #contar puntuacion
        if i.isdigit()==False and i.isalpha()==False and i!=" ":
            puntuacion+=1
        #contar letras
        if i.isalpha()==True:
            letras+=1    
    #eliminar puntuacion
        if  i.isalpha()==True or i==" ":
            L_sinPuntos.append(i)
    sin_puntos=("".join(L_sinPuntos)).split(" ")
    #contar palabras
    for i in sin_puntos:
        if i.isalpha()==True:
            palabras+=1
    #calcular largo promedio
    largo_promedio=letras/palabras
    #calcular espacios
    for i in frase:
        if i==" ":
            espacios+=1
    return palabras, Caracteres, largo_promedio, espacios, puntuacion
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))