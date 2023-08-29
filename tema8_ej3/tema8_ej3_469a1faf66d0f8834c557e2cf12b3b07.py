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
    count = 0
    caracteres = len(frase)
    for i in frase:
        if i == " ":
            count = count + 1
    
    
    textos = frase.split()
    j = 0
    promedio = 0
    while j < len(textos):
        promedio = promedio + len(textos[j])
        j += 1
        
    promedio = (promedio-3) / 75
    
    textos = frase.split()
    j = 0
    while j < len(textos):
        texto = textos[j]
        if texto == "estonoesunmeme":
            break
        j += 1
        
    acento = 0
    for i in frase:
            if i == "." or i == ":" or i == ";" or i == ",":
                acento = acento + 1 
            
    
    return j, caracteres, promedio, count, acento

if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         