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
    lista_frase1 = list(frase)
    lista_frase2 = frase.split()
    lista_borr1 = []
    for i in lista_frase2: 
        if '.' in i:
            lista_borr1.append(i)
    borr = ''.join(lista_borr1)
    lista_borr3 = list(borr)
    for i in lista_borr3:
        if i == '.':
            lista_borr3.remove(i)
    lista_borr3.remove(lista_borr3[-1])
    borr1 = ''.join(lista_borr3)
    lista_frase2.remove(lista_frase2[-1])
    lista_frase2.append(borr1)
    n_palabras = len(lista_frase2)
    n_caracteres = len(lista_frase1)
    lista_largos = []
    for i in lista_frase2:
        lista_largos.append(len(i))
    suma_largos = 0
    for i in lista_largos:
        suma_largos += i
    largo_promedio = suma_largos / len(lista_largos)
    n_espacios = frase.count(' ')
    lista_puntuacion = [',','.',':',';']
    puntuaciones = 0
    for i in lista_frase1:
        if i in lista_puntuacion:
            puntuaciones += 1

    return n_palabras, n_caracteres, largo_promedio, n_espacios, puntuaciones

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
