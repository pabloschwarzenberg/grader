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
    #numPalabras
    numPalabras = 0
    if frase[0].isalpha() or frase[0] == "\n":
        numPalabras = 1
    for i in range(len(frase)):
        if frase[i] == " ":
            numPalabras += 1
            i += 1
        if frase[i - 1].isalpha() and frase[i] == "\n":
            numPalabras += 1
            i += 1
    #numCaracteres
    listaLetras = []
    for l in frase:
        if l.isalpha() and l not in listaLetras:
            listaLetras.append(l)
    listaPrueba = listaLetras
    listaLetras.append(" ")
    listaLetras.append("\n")
    listaLetras.append(".")
    numCaracteres = 0
    for letra in frase:
        if letra in listaLetras:
            numCaracteres += 1
    #largo Promedio de las Palabras
    listaPal = []
    listaPal1 = []
    listaFinal = []
    pal = ""
    for lit in frase:
        if lit in listaPrueba:
            pal += lit
            if lit == " ":
                pal = pal.strip()
                listaPal.append(pal)
                pal = ""
    for palabra in listaPal:
        palabra = palabra.split("\n")
        listaPal1.append(palabra)
    for num in listaPal1:
        if len(num) == 1:
            n = 1
        if len(num) == 2:
            n = 2
        for pal in range(n):
            listaFinal.append(num[pal])
    largo = []
    for palabras in listaFinal:
        largo.append(len(palabras))
    total = sum(largo)
    promedio = total/len(listaFinal)
    promedioFinal = round(promedio, 2)   
    #numEspacios
    numEspacios = 0
    for let in frase:
        if let == " ":
            numEspacios += 1
    #numPuntos
    numPuntos = 0
    for letras in frase:
        if letras == ".":
            numPuntos += 1

    return numPalabras, numCaracteres, promedioFinal, numEspacios, numPuntos
         