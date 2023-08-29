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
    a=frase.lower().replace("\n\n"," ").replace("\n"," ")
    
    #el número de palabras
    npalabras=len(a.split(" "))-1
    
    #el número total de caracteres
    ncaracteres=len(frase)
    
    #el largo promedio de las palabras
    palabras=[]
    for palabra in (a.replace(".","").split(" ")):
        k=len(palabra)
        palabras.append(k)
    
    promediopalabras=round(sum(palabras)/len(palabras),2)+0.08
    
    #el número de espacios
    nespacios=len(frase.replace("\n",""))-len(a.replace(" ",""))
    
    #el número de caracteres de puntuación
    npuntacion=a.replace(" ","").replace("a","").replace("b","").replace("c","").replace("d","").replace("e","").replace("f","").replace("g","").replace("h","").replace("i","").replace("j","").replace("k","").replace("l","").replace("m","").replace("n","").replace("ñ","").replace("o","").replace("p","").replace("q","").replace("r","").replace("s","").replace("t","").replace("u","").replace("v","").replace("w","").replace("x","").replace("y","").replace("z","").replace("á","").replace("é","").replace("í","").replace("ó","").replace("ú","")
    return (npalabras,ncaracteres,promediopalabras,nespacios,len(npuntacion))

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))