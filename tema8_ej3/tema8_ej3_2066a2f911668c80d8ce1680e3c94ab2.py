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
    p = frase.split()
    p_num = len(p)
    c_num = sum(signo in frase for signo in frase)
    lp = (sum(len(palabra) for palabra in p) - sum(signo in '.,:;?!¿¡' for signo in frase)) / p_num
    es_num = frase.count(" ")
    pt_num = sum(signo in '.,:;?!¿¡' for signo in frase)

    return p_num, c_num, lp, es_num, pt_num

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         