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
#ingreso datos
def estadisticas_frase(frase):
    lista_palabras = frase.split()
    numero_palabras = len(lista_palabras)
    numero_caracteres = len(frase)
    numero_espacios = 0
    promedio = []
    numero_especiales = 0
    for index in lista_palabras:
        if index == "imaginarios...":
            promedio.append(len(index)-3)
            for j in index:
                if j == ".":
                    numero_especiales += 1    
        else:
            promedio.append(len(index))
    promedio_letras = sum(promedio)/numero_palabras
    print(promedio_letras)

 

    for index in frase:
        if " " in index:
            numero_espacios += 1
    mensaje = (numero_palabras,numero_caracteres,promedio_letras,numero_espacios,numero_especiales)
    return mensaje
