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

def buscarTodas_for(a,b):
    apariciones=[]
    for i in range(0,len(a)):
        if a[i]==b:
            apariciones.append(i)
    return apariciones
def estadisticas_frase(s):
    palabras=s.split(" ")
    suma_largos=0
    for i in palabras:
        suma_largos+=len(i)
    numero_palabras=len(palabras)
    largo_promedio_palabra=suma_largos/len(palabras)
    numero_espacios=len(buscarTodas_for(s," "))
    numero_total_caracteres=len(s)
    puntuacion=".:,;-_{[}]+*´¨'\!#$%&/()=¿¡?"
    numero_puntuacion=0
    for i in s:
        if i in puntuacion:
            numero_puntuacion+=1
    return numero_palabras,numero_total_caracteres,largo_promedio_palabra,numero_espacios,numero_puntuacion


if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         