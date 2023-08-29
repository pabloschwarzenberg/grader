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
    lista = []
    string = ""
    espacios = frase.count(" ")
    puntos = frase.count(".")
    string=frase.replace("\n"," ")
    string2=string.replace("."," ")
    string3=string2.replace("'"," ")
    string4=string3.split(" ")
    
    for i in range (0,len(string4)):
        if string4[i]!="":
            lista.append(string4[i])
        

    numeropalabras=len(lista)
    suma=0    
    for j in range(0,len(lista)):
        suma=suma+len(lista[j])
    promedio_palabras=(suma/len(lista))
    caracteres=len(frase)
       


    return numeropalabras,caracteres,promedio_palabras,espacios,puntos

if __name__ == "__main__":
    
    print(estadisticas_frase(hombre_imaginario))
         