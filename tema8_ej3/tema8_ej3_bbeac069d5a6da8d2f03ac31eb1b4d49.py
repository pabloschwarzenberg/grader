hombre_imaginario = ("""
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
circundado de cerros imaginarios...""")

def estadisticas_frase(texto):
    texto = texto.lower()
    nCaracteres = len(texto)
    nPalabras = len(texto.split()) 
    espacios = 0
    especial = 0
    for l in texto:
        if l == " ":
            espacios += 1
        if l != " " and (l < "a" or "z" < l) and l != "\n":
            if l == "á":
                l = "a"
            elif l == "é":
                l = "e"
            elif l == "í":
                l = "i"
            elif l == "ó":
                l = "o"
            elif l == "ú":
                l = "u"
            else:
                especial += 1
    texto = texto.strip(".")
    promPalabras = []
    for p in texto.split():
        promPalabras.append(len(p))
    prom = sum(promPalabras) / len(promPalabras)
    return nPalabras,nCaracteres,prom,espacios,especial
    
print(estadisticas_frase(hombre_imaginario))