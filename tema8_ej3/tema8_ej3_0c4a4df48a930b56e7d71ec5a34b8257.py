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
    largos=0
    enter=0
    vocales =0
    palabras=0
    espacios=0
    con=0
    s=0
    carpun=['.',',',';',':']
    c=['b','c','d','f','g','h','j','k','l','m','n','ñ','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','Ñ','P','Q','R','S','T','V','W','X','Y','Z']
    a=['a','e','i','o','u','A','E','I','O','U','á','é','í','ó','ú']
    for i in frase:
        if i in c:
            con=con+1
        elif i in a:
            vocales+=1
        elif i==' ':
            espacios+=1
        elif i=='\n':
            enter+=1
        else:
            s+=1
    
    palabras=espacios+1
    largo_promedio=(con+vocales+enter+s)/palabras
    
       
       
                
    print('numero de palabras es ',palabras)
    print('numero total de caracteres es ',con+vocales+s+espacios+enter)
    print('largo promedio es ',largo_promedio)
    print('numero de espacios es ',espacios)
    print('numero de carateres de puntuacion es ',s)
    return palabras,con+vocales+s+espacios+enter,largo_promedio,espacios,s
    
    pass

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))

