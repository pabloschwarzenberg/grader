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
    frase=frase.lower()
    tildes=[["á","a"],["é","e"],["í","i"],["ó","o"],["ú","u"]]
    i=0
    esp=" "
    carac="abcdefghijklmnñopqrstuvwxyz,;.:-¡!¿? \n"
    letra="abcdefghijklmnñopqrstuvwxyz"
    puntuacion=",;.:-¡!¿?"
    cantesp=0
    cantletra=0
    cantidadpalabra=0
    cantcarac=0
    cantpuntuacion=0
    frase=frase.strip()
    tamanopal=[]
    letrapal=""
    for elem in tildes:
        frase=frase.replace(elem[0],elem[1])
    frase=frase.lower()
    while i<len(frase):
        if i==0:
            letrapal+=frase[i]
            j=i
            while frase[j+1] in letra:
                letrapal+=frase[j+1]
                j+=1
            tamanopal.append(letrapal)
            letrapal=""
        if frase[i]=="\n":
            cantidadpalabra+=1
        if frase[i]==esp:
            cantesp+=1
            cantidadpalabra+=1
        if frase[i]==esp or frase[i]=="\n":
            j=i
            while frase[j+1] in letra:
                letrapal+=frase[j+1]
                j+=1
            tamanopal.append(letrapal)
            letrapal=""
        if frase[i] in letra:
            cantletra+=1
        if frase[i] in carac:
            cantcarac+=1
        if frase[i] in puntuacion:
            cantpuntuacion+=1
        i+=1
    elem=0
    suma=0
    cantidadpalabra-=1
    cantcarac+=1
    while elem<len(tamanopal):
        suma+=len(tamanopal[elem])
        elem+=1
    promediopal=suma/cantidadpalabra
    return cantidadpalabra,cantcarac,promediopal,cantesp,cantpuntuacion
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         