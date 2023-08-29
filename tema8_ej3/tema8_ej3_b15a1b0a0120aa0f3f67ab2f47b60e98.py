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

def estadisticas_frase(s):
    palabras=0
    espacios=0
    caracteres=0
    caracteres_especiales=0
    palabra=""
    largos=[]
    inicio_palabra=False
    frases=s.split("\n")
    for i in frases: ### Primero contemos letras, puntuación y espacios
        for j in i:
            if j.isalpha(): ### Revisa si un caracter es una letra o no
                inicio_palabra=True
                caracteres+=1
            elif j==" ":
                espacios+=1
            else:
                caracteres_especiales+=1
##############################################################
            if j.isalpha():
                palabra+=j
            else:
                if inicio_palabra:
                    palabras+=1
                    largos.append(len(palabra))
                inicio_palabra=False
                palabra=""
        if palabra.isalpha():
            palabras+=1
            largos.append(len(palabra))
            inicio_palabra=False
            palabra=""
    promedio=(sum(largos)/len(largos))
    
    return(" Numero de palabras: {} \n Numero de letras + espacios = {} \n Largo Promedio = {} \n Numero de espacios = {} \n Numero de caracteres especiales = {}".format(palabras,caracteres+espacios,promedio,espacios,caracteres_especiales))
    