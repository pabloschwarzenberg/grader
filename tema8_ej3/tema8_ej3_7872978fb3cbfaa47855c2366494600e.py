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
    CaracteresTotales = 0
    for i in frase:
        CaracteresTotales+=1
    
    frase = frase.split("\n")
    texto = ''
    sig = [',','.',';',':','_','-','?','!']

   
    
    NumeroDeEspacios = 0
    CaracteresPuntuacion = 0

    for oraciones in frase:
        if oraciones != '':
            for letras in oraciones:
                if letras == ' ':
                    NumeroDeEspacios += 1
            texto += oraciones+' '

    texto = texto.split('.')
    for a in texto:
        if a == '' or a == ' ':
            CaracteresPuntuacion +=1
        else:
            texto = a

    texto = texto.split()
    NumeroDePalabras = len(texto)
    listadepalabras = []

    for palabras in texto:
        letras = len(palabras)
        listadepalabras.append(letras)

    PromedioPalabras = (sum(listadepalabras))/NumeroDePalabras
    
    return NumeroDePalabras,CaracteresTotales,PromedioPalabras,NumeroDeEspacios,CaracteresPuntuacion