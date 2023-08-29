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
    caracteres = len(frase)
    num_espacios  = 0
    num_puntiacion = 0
    j = " "
    for j in frase:
        if j == " ":
            num_espacios = num_espacios + 1
        if j == ".":
            num_puntiacion = num_puntiacion +1
    frase = frase.strip(".")
    palabras = len(frase.split())
    
    l_prom = list(frase.split())
    sumatoria = 0
    suma = 0 
    for i in range(palabras):
        sumatoria = len(l_prom[i])
        i = i + 1
        suma = suma + sumatoria
    promedio = suma/palabras
    return palabras, caracteres, promedio, num_espacios, num_puntiacion
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))

def decodificar(men):
    ##
    a = str(men[0:8])
    dec1=(int(str(a), 2))
    l1=chr(dec1)
    ##
    b = str(mensaje[10:17])
    dec2=(int(str(b), 2))
    l2=chr(dec2)
    ##
    c = str(mensaje[19:26])
    dec3=(int(str(c), 2))
    l3=chr(dec3)
    ##
    d = str(men[28:35])
    dec4=(int(str(d), 2))
    l4=chr(dec4)
    p = l1+l2+l3+l4
    return p
if __name__ == "__main__":
    men=deco("01101000,01101111,01101100,01100001")
    print(men)