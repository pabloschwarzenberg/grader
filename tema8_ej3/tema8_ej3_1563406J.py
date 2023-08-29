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
import math
def estadisticas_frase(frase):
    b=len(frase)
    print("Su cantidad de caracteres es: ",b)
    x=frase.split()
    d=len(x)
    print("La cantidad de palabras es: ",d)
    z=" "
    i=0
    ii=00
    r="qwertyuiopñlkjhgfdsazxcvbnm1234567890 "
    for c in frase:
        if r.find(c)==-1:
            ii=ii+1
        if c==z:
            i=i+1
    print("La cantidad de espacios es: ",i)
    print("La cantidad de signos de puntuacion es: ",ii)
    promedio=(b-i-ii)/d
    prom=math.floor(promedio)
    print("El largo promedio de las palabras es: ",prom)
    return d,b,prom,i,ii

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         