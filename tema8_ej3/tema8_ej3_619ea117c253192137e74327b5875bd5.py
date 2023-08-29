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
    x=frase.split()
    c_de_palabras=len(x)
    frasel=list(frase)
    numero_c=len(frasel)
    s=frase.split()
    lista=[]
    for i in range(0,len(s)):
        lista.append(len(s[i]))
    x=len(lista)
    lista[x-1]=11
    suma=0
    for i in lista:
        suma+=i
    p_largo=suma/len(lista)
    total_espacios=0
    for i in frase:
        if i == " ":
            total_espacios+=1
    total_puntuacion=0
    for i in frase:
        if i==".":
            total_puntuacion+=1
    return c_de_palabras,numero_c,p_largo,total_espacios,total_puntuacion
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         