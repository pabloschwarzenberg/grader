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
def totalCaracteres(lista):
    suma=0
    for cadenas in lista:
        if cadenas!="":
            suma+=len(cadenas)
    return suma
def cantPalabras(lista):
    palabras=0
    for cadenas in lista:
        if cadenas!="":
            palabras+=1
    return palabras
def promedioLargo(lista):
    largo=cantPalabras(lista)
    promedio=0
    for cadenas in lista:
        largoCadena=0
        if cadenas!="":
            if not cadenas.isalpha():
                for caracteres in cadenas:
                    if caracteres.isalpha():
                        largoCadena+=1
                print(largoCadena)
            else:
                largoCadena=len(cadenas)
        promedio+=largoCadena
    promedio/=largo
    return promedio
def caracteresEspeciales(lista):
    caracteresEsp=0
    for cadena in lista:
        if not cadena.isalpha():
            for caracter in cadena:
                if not caracter.isalpha():
                    caracteresEsp+=1
    return caracteresEsp
def estadisticas_frase(frase):
    cadena=frase.split("\n") 
    separador=" "
    frase2=separador.join(cadena)
    cadena2= frase2.split(" ")
    largo=cantPalabras(cadena2)
    promedio=promedioLargo(cadena2)
    caracteres=totalCaracteres(frase2)
    espacios=frase.count(" ")
    caracteresEsp=caracteresEspeciales(cadena2)
    return (largo,caracteres,promedio,espacios,caracteresEsp)

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         