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


def numero_de_palabras(frase):
    frase = frase.replace('\n', ' ')
    frase = ''.join(frase)
    frase = frase.split(' ')
    while '' in frase:
        frase.remove('')
    a = 0
    for i in frase:
        a += 1
    return a


def numero_total_de_caracteres(frase):
    return len(frase)


def largo_promedio_de_las_palabras(frase):
    frase = frase.replace('\n', ' ')
    frase = ''.join(frase)
    frase = frase.split(' ')
    while '' in frase:
        frase.remove('')
    sum = 0
    for i in frase:
        if i[-3:] == '...':
            sum += len(i) - 3
            continue
        sum += len(i)
    prom = sum / len(frase)
    return prom


def numero_de_espacios(frase):
    frase = frase.splitlines()
    while '' in frase:
        frase.remove('')
    a = 0
    for i in frase:
        a += i.count(' ')
    return a


def numero_de_caracteres_de_puntuacion(frase):
    frase = frase.replace('\n', ' ')
    frase = ''.join(frase)
    frase = frase.split(' ')
    while '' in frase:
        frase.remove('')
    a = 0
    for i in frase:
        if '.' in i:
            a += i.count('.')
        elif ',' in i:
            a += i.count(',')
    return a


def estadisticas_frase(frase):
    a = numero_de_palabras(frase)
    b = numero_total_de_caracteres(frase)
    c = largo_promedio_de_las_palabras(frase)
    d = numero_de_espacios(frase)
    e = numero_de_caracteres_de_puntuacion(frase)
    return a,b,c,d,e
    
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         