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
    a=s.split()
    numeropalabras=len(a)
    numerocaracteres=len(s)
    suma=0
    for i in a:
        if i.isalpha()==True:
            suma+=len(i)
        else:
            palabra=''
            for j in i:
                if j.isalpha()==True:
                    palabra=palabra+j
            print(palabra)
            suma+=len(palabra)
    largop=suma/numeropalabras
    sumaespacios=0
    sumasignos=0
    for i in s:
        if i==' ' :
            sumaespacios+=1
        if i=='.' or i==';' or i==':' or i==';' or i==',':
             sumasignos+=1

             
    return numeropalabras, numerocaracteres, largop, sumaespacios,sumasignos

    

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         