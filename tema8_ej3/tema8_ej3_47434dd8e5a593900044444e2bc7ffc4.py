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
    lista=list(frase)
    espacios=frase.count(" ")
    caracteres=len(frase)
    i=0
    while i!=len(lista)-1:
        if lista[i]=="\n" and lista[i+1]=="\n":
            lista.remove(lista[i+1])
        elif lista[i]=="\n" and lista[i+1]!="\n":
            lista.remove(lista[i])
            lista.insert(i," ")
            i+=1
        else:
            i+=1
    frase="".join(lista)
    frase=frase.strip()
    palabras=len(frase.split(" "))

    frase=frase.lower()
    lista2=frase.split(" ")
    abc="abcdefghijklmnopqrstuvwxyzáéíóú"
    j=0
    for elemen in lista2:
        for letra in list(elemen):
            if letra in abc:
                j+=1
    promedio=j/palabras

    puntuacion=len(frase)-frase.count(" ")-j

    return palabras, caracteres, promedio, espacios, puntuacion

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         