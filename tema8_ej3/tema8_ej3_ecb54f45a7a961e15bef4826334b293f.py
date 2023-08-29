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

def estadisticas_frase1(s):
    b=list(s)
    while True:
        if "." in b:
            b.remove(".")
        if " " in b:
            b.remove(" ")
        else:
            break
    #print(b)
    a=len(b)
    return a
def estadisticas_frase2(s):
    c=list(s)
    while True:
        if "." in c:
            c.remove(".")
        else:
            break
    e = "".join(c)
    r=e.split(" ")
    return (len(r))
def estadisticas_frase3(s):
    c=list(s)
    l=[]
    while True:
        if "." in c:
            l.append(".")
            c.remove(".")
        else:
            break
    return (len(l))
def estadisticas_frase4(s):
    b = list(s)
    l=[]
    while True:
        if " " in b:
            l.append(" ")
            b.remove(" ")
        else:
            break
    return (len(l))
#print(estadisticas_frase1(t))
#print(estadisticas_frase2(t)/estadisticas_frase1(t))
#print(estadisticas_frase3(t))
#print(estadisticas_frase4(t))

if __name__ == "__main__":
    print(estadisticas_frase1(hombre_imaginario))