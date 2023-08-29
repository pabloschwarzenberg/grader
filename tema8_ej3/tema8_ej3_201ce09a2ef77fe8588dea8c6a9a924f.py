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
    total_ch = len(frase)
    frase= 0
    espacio=0
    palabra= 0
    punct = 0
    frase = frase.split('\n')
    for linea in frase:


        if linea!= '':
            linea = linea.split('')
            espacio+= len(linea) -1
            for palabra in linea:
                palabra+= 1
                for letra in palabra:
                    if letra.isalnum():
                        letra+= 1
                    else:
                        punct+= 1
    prom= letra/ palabra
    return (palabra, total_ch, prom, espacio, punct)                    
estadisticas_frase(hombre_imaginario)                
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         