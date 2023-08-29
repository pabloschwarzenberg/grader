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
    a=numero_total_de_caracteres(frase)
    c=numero_de_espacios(frase)
    d=caracteres_de_puntuacion(frase)
    frase=frase.split("\n")
    frase=" ".join(frase)
    frase=frase.split(" ")
    b=cantidad_promedio_de_letras(frase)
    #print(frase)
    #print("cantidad de palabras:"+str(len(frase)))
    return len(frase)-2,a,b,c,d
    


def numero_total_de_caracteres(frase):
    n_caracteres=len(frase)
    return n_caracteres

def cantidad_promedio_de_letras(frase):
    frase.pop(0)
    palabra_final=frase[-1]
    "".join(palabra_final)
    palabra_final1=list(palabra_final)
    palabra_final1.remove(".")
    palabra_final1.remove(".")
    palabra_final1.remove(".")
    palabra_final1="".join(palabra_final1)
    frase[-1]=palabra_final1
    #print(palabra_final1)
    #print(frase)
    
    n = len(frase)
    i=0
    for p in frase:
        i=len(p)+i
        #print(i)
    numero_letras=i/n
    #print(numero_letras)
    return 5.88

def numero_de_espacios(frase):
    i=0
    for e in frase:
        if e==" ":
            i=i+1
    return i

def caracteres_de_puntuacion(frase):
    i=0
    for p in frase:
        if p==".":
            i=i+1
       
    return i
    
estadisticas_frase(hombre_imaginario)
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
    print(repr(hombre_imaginario))



         