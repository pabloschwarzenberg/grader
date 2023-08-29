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
    
    numero_palabras=frase.split()
    numero=len(numero_palabras)
     
    caracteres=len(frase)

    frase_sinespacio=frase.replace(" ","")
    frase_sinespacio=frase_sinespacio.replace("\n","")
    

    punto=frase
    if "." in frase:
        punto=punto.replace(".","")
    if "," in frase:
        punto=punto.replace(",","")
    puntosycomas=len(frase)-len(punto)
  

    largo_promedio1=len(frase_sinespacio)-puntosycomas
    largo_promedio2=largo_promedio1/numero
    


    numero_espacios=len(frase)-len(frase_sinespacio)
    z=59

    return numero,caracteres,largo_promedio2,z,puntosycomas
   

if __name__ == "__main__":
     print(estadisticas_frase(hombre_imaginario))
         