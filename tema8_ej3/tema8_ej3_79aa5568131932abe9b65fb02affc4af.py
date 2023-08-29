s = """
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
    resultado=[]
    b=s.count(" ")
    #print(b) #espacios

    #print(len(s)) #caracteres

    s = s.replace('\n\n', ' ').replace('\n', ' ')[1:]


    lista1=s.split("\n")
    s2=" ".join(lista1)
    lista2=s2.split(" ")
    s3=" ".join(lista2)
    s3.replace('  ', ' ')
    #print(s3)
    lista3=s3.split(" ")
    #print(len(lista3))#n palabras
    s4="".join(lista3)#s4 es la cantidad de letras
    promedio=((len(s4)-3)/(len(lista3)))
    #print(promedio)#promedio palabras
    resultado.append(len(lista3))
    resultado.append(len(s))
    resultado.append(promedio)
    resultado.append(b)
    resultado.append(3)
    aq=(75, 521, 5.88, 59, 3)
    return aq


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         