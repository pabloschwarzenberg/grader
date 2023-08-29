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
    a=0
    b=len(s) #total de caracteres
    c=s.count(' ') #total de espacios

    d=s.split("\n")
    #print(d)
    contador=0
    for i in d:
        if i !='':
            contador=len(i.split(" "))+contador
            #print(i.split(" "))
   #cantidad de palabras



    f1=s.count('.')
    f2=s.count('!')
    f3=s.count('¡')
    f4=s.count('¿')
    f5=s.count('?')
    
    puntuacion=f1+f2+f3+f4+f5

    g=s.split(" ")

    
    
    letras=0
    cantidad_puntos=s.count('.')
    for palabra in g:
        palabra_split = palabra.split('\n')
        for i in palabra_split:
            letras=letras+len(i)
    h=(letras-cantidad_puntos)/contador #largo promedio de palabras'''

    return contador,b,h,c,puntuacion

                      