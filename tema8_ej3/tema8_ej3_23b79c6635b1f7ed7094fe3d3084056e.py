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
    
    palabradividida = frase.split()
    cantidaddepalabras = len(palabradividida)
    largospromedios = 0
    ntotaldecaracteres = 0
    cantidadespacios = 0
    caracterespuntos = 0
    mensaje = ""
    
    for i in (frase):
        ntotaldecaracteres += 1
        
    for i in (frase):
        if (i == " "):
            cantidadespacios += 1
            
    for j in (frase):
        if (j == "."):
            caracterespuntos += 1      
            
    for i in range (cantidaddepalabras):
        largospromedios += len(palabradividida[i])
            
    largospromedios -= caracterespuntos
    largospromedios /= cantidaddepalabras
    
    mensaje += "("
    mensaje += str(cantidaddepalabras)
    mensaje += ","
    mensaje += str(ntotaldecaracteres)
    mensaje += ","
    mensaje += str(largospromedios)
    mensaje += ","
    mensaje += str(cantidadespacios)
    mensaje += ","
    mensaje += str(caracterespuntos)
    mensaje += ")"
    return (mensaje)
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         