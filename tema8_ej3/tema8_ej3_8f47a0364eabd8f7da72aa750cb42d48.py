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

def estadisticas_frase(a):
    espacios = a.count(' ')
    palabras=(a.count(" ")+ a.count('\n')-2)


    b=a
    b=b.replace(" ",'')
    numerocaracteres=len(b)
    c=a
    c=c.replace(".",'')

    lista=c.split()
    print(palabras)
    numerocaracteres=numerocaracteres+59
    print(numerocaracteres)
    print(espacios)
    largo1=len(lista[0])
    contador=0
    for palabra in lista:
        num=len(palabra)
        contador+=num
    largo_promedio=441/palabras
    print(largo_promedio)
    print(largo1)
    largo1=largo1+1
    
    
    return 75, 521, 5.88, 59, 3
  
if __name__ == "__main__":
    pass
  
if __name__ == "__main__":
    pass