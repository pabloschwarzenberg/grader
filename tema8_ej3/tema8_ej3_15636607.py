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
    b=(len(frase))
    d=frase.count(' ')
    frase=frase.split()
    a=(len(frase))
    p=0
    for palabra in frase:
        p=p+palabra.count('.')
        p=p+palabra.count(',')
        p=p+palabra.count(';')
        p=p+palabra.count(':')
        p=p+palabra.count('!')
        p=p+palabra.count('¡')
        p=p+palabra.count('?')
        p=p+palabra.count('¿')
    e=p
    n=0
    for i in range(0,(a-1)):
        n=n+len(frase[i])
    c=(n-p)/a
    return a,b,c,d,e
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         