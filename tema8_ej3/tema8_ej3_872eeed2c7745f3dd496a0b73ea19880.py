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

    p=len(frase)

    print(p)

    espacios=frase.count(" ")

    print(espacios)

    l=frase.split()

    comas=frase.count(",")

    puntos=frase.count(".")

    punto_coma=frase.count(";")

    dos_puntos=frase.count(":")

    puntuacion=comas+puntos+punto_coma+dos_puntos

    número_palabras=len(l)

    i=0

    while i<len(l):

        s=l[i]

        s2=""

        r=0

        while r<len(s):

            a=s[r]

            if (a!="." and a!=",") and (a!=";" and a!=":"):

                s2=s2+a

            r=r+1

        l[i]=s2

        i=i+1


    z=0

    suma=0

    while z<len(l):

        caracteres=len(l[z])

        suma=suma+caracteres

        z=z+1


    suma=int(suma)

    número_palabras=int(número_palabras)

    promedio=(suma)/(número_palabras)

    total=suma + espacios + puntuacion

    return (número_palabras, p, promedio, espacios, puntuacion)



if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         
