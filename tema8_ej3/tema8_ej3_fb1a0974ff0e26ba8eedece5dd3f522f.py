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
    caracteres = 0
    palabras = 0
    suma_largos = 0
    espacios = 0
    puntuacion = 0
    frase1 = ""
    frase2 = ""
    l_frase = frase.splitlines()
    for i in frase:
        if i != " " and i != "\n":
            frase1 = frase1 + i

    for i in frase:
        if i != "\n":
            frase2 += i
        else:
            frase2 += " "

    frase1 = frase1.strip()
    frase2 = frase2.strip()

    for i in frase:
        caracteres += 1

    l_frase2 = frase2.split(" ")
 

    for i in l_frase2:
        if not(i in [" ","\n",""]):
            suma_largos += len(i)
            palabras += 1
            

    for i in frase:
        if i == " ":
            espacios += 1
            
        if (not i.isalpha()) and not(i in [" ","\n",""]):
            puntuacion += 1



    largo_promedio = float(suma_largos)/float(palabras)
        
    return(palabras,caracteres,largo_promedio,espacios,puntuacion)
         