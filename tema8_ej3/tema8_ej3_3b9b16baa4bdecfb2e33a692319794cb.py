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
    puntos= s.count(".")
    ncaracteres=len(s)
    espacios= s.count(" ")
    s=s.replace("\n\n"," ")
    s=s.replace("\n"," ")
    s=s.lower()
    s=s.replace("á","a")
    s=s.replace("é","e")
    s=s.replace("í","i")
    s=s.replace("ó","o")
    s=s.replace("ú","u")
    s=s.split(" ")
    espaciosblanco=s.count(" ")
    cantidadpalabra= len(s)-1
    n=0
    for i in s:
        i=i.replace(".","")
        n+=len(i)
    promedio= round((n/(len(s)-1)),2)
    print(s)
    return (cantidadpalabra,ncaracteres,promedio,espacios,puntos)




if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))