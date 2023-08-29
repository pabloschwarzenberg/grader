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
    frases=frase
    frases=frases.replace(" ","")
    esp=len(frases)
    frases=frases.replace(" ","")
    frases=frases.replace(".","")
    frases=frases.replace(",","")
    frases=frases.replace(".","")
    frases=frases.replace(":","")
    frases=frases.replace(";","")
    frases=frases.replace("?","")
    frases=frases.replace("!","")
    ori3=len(frases)
    orig=len(frase)
    listaP=frase.split()
    Palabras=len(listaP)
    frase=frase.replace("\n"," ")
    frase=frase.replace(" ","")
    frase=frase.replace(".","")
    frase=frase.replace(",","")
    frase=frase.replace(".","")
    frase=frase.replace(":","")
    frase=frase.replace(";","")
    frase=frase.replace("?","")
    frase=frase.replace("!","")
    
    ori2=len(frase)
    promedio=ori2/Palabras
    espacios=orig-esp
    f=orig-(espacios+ori3)
    return (Palabras,orig,promedio,espacios,f)

if __name__ == "__main__":

    print(estadisticas_frase(hombre_imaginario))      