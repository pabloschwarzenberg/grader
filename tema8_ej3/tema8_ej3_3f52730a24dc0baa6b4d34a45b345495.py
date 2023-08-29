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
    #numero caracteres y espacios:
    caracteres_puntuacion=0
    carac_tot=0
    num_espacios=0
    for i in list(s):
        if i=="." or ",":
            caracteres_puntuacion+=1
            carac_tot+=1
        elif i==" ":
            num_espacios+=1
        else:
            carac_tot+=1
    
    #caracteres totales:
    caracteres_totales=carac_tot-num_espacios

    #numero palabras:
    num_palabras=len(list(s.split(" ")))

    #largo promedio palabras:
    largo_prom=(caracteres_totales-caracteres_puntuacion)/num_palabras

    return print("N° Palabras: ",num_palabras,"N° Carac. Totales: ",caracteres_totales,"Largo Promedio: ",largo_prom,"N° Espacios: ",num_espacios,"N° Carac. Puntuacion: ",caracteres_puntuacion)

if __name__ == "__main__":
    estadisticas_frase(hombre_imaginario)
         