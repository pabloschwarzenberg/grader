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
    cont=0
    caracteres=len(frase)
    espacios=frase.count(' ')
    frase_a=frase.split('\n')
    i=0
    for c in frase_a:
        if c!='':
            i+=len(c.split(' '))
    punto=frase.count('.')
    exclamacion_i=frase.count('¡')
    exclamacion_f=frase.count('!')
    interrogacion_i=frase.count('¿')
    interrogacion_f=frase.count('?')
    total=punto+exclamacion_i+exclamacion_f+interrogacion_i+interrogacion_f
    frase_b=frase.split(' ')
    letras=0
    puntos=frase.count('.')
    for p in frase_b:
        p_split=p.split('\n')
        for x in p_split:
            letras+=len(x)
    largo_prom=(letras-puntos)/i
    
    return i,caracteres,largo_prom,espacios,total
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         