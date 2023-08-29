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
    num_tot_caracteres=len(frase)
    lista_p=frase.split()
    num_palabra=len(lista_p)
    num_espacios=frase.count(' ')
    num_p=frase.count(".")
    num_c=frase.count(",")
    num_puntuacion= num_p + num_c
    b=0
    for i in lista_p[:num_palabra-1]:
        b=b+(len(i))
    promedio=(b+11)/num_palabra
        
    
    return num_palabra, num_tot_caracteres, promedio, num_espacios, num_puntuacion

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         