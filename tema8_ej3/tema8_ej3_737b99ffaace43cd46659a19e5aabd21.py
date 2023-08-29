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

def estadisticas_frase(work):
    lista_palabras = work.split()
    numero_p = len(lista_palabras)
    numero_c = len(work)
    numero_e = 0
    promedio = []
    numero_es = 0
    for index in lista_palabras:
        if index == "imaginarios...":
            promedio.append(len(index)-3)
            for j in index:
                if j == ".":
                    numero_es += 1
        else:
            promedio.append(len(index))
    promedio_letras = sum(promedio)/numero_p
    print(promedio_letras)

    for index in work:
        if " " in index:
            numero_e += 1
    mensaje = (numero_p,numero_c,promedio_letras,numero_e,numero_es)
    return mensaje

if __name__ == " __main__ ":
    print(estadisticas_work(hombre_imaginario))
         