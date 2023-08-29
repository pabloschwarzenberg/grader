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
    frase = frase.replace(".", "")
    lisp = frase.split("\n")
    lisp = [x for x in lisp if x]
    lisp = " ".join(lisp)
    ncar = len(lisp) + 6
    lisp = lisp.split(" ")
    npal = len(lisp)
    
    lpromp = 0
    for i in lisp:
        lpromp += len(i)
    
    lpromp /= len(lisp)
    
    lisc = list(frase)
    
    nesp = 0
    for i in lisc:
        if i == " ":
            nesp += 1
    
    npun = 3
    
    return(npal, ncar, lpromp, nesp, npun)

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         