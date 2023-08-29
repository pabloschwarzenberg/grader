hombre_imaginario = """
El hombre imaginario
vive en una mansiÃ³n imaginaria
rodeada de Ã¡rboles imaginarios
a la orilla de un rÃ¬o imaginario
De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios
Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcÃ³n imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""
def estadisticas_frase(frase):
    caracteres = len(frase)
    num_espacios = 0
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

    print(estadisticas_frase(hombre_imaginario))


# In[ ]:


def decodificar(mensaje):
    a = str(mensaje[0:8])
    decimal1=(int(str(a), 2))
    letra1=chr(decimal1)
    b = str(mensaje[10:17])
    decimal2=(int(str(b), 2))
    letra2=chr(decimal2)
    c = str(mensaje[19:26])
    decimal3=(int(str(c), 2))
    letra3=chr(decimal3)
    d = str(mensaje[28:35])
    decimal4=(int(str(d), 2))
    letra4=chr(decimal4)
    palabra = letra1+letra2+letra3+letra4
    return palabra

    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)