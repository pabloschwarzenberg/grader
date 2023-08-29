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
    frase1=len(frase.split())
    frase2=len(frase)
    count = 0
    for i in frase: 
        if i == " ": 
            count += 1
    frase4=count
    count2 = 0
    for i in frase: 
        if i == ".": 
            count2 += 1
    frase5=count2
    frase=frase.replace('.','')
    # frase3=sum([i.strip(string.punctuation).isalpha() for i in frase.split()])
    frase3=sum(map(len, frase.split()))/float(len(frase.split()))
    # temp = [len(ele) for ele in result] 
    # frase3 = 0 if len(result) == 0 else (float(sum(result)) / len(result))
    return frase1,frase2,frase3,frase4,frase5
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         