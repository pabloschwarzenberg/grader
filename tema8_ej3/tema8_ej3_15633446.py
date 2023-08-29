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

def estadisticas_frase(s):
    numero_caracteres=len(s)
    caracteres_puntuacion=0
    for k in range(0,len(s)):
        p=s[k]
        if(p==".")or(p==",")or(p==";"):
            caracteres_puntuacion +=1
    s=s.split()
    numero_palabras=len(s)
    numero_espacios=len(s)-1
    suma=0
    for i in range(0,len(s)):
        palabra=s[i]
        largo=len(palabra)
        suma=suma+len(palabra)
    largo_promedio=suma/len(s)
    return(numero_caracteres,numero_palabras,largo_promedio,caracteres_puntuacion)

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         